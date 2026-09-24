from datetime import datetime

from app.services.runtime import runtime_warned
from app.config import GRACE_PERIOD
from app.database.database import (
    get_user,
    save_user,
    already_warned,
    mark_warned,
    needs_recheck,
    record_stat,
    get_last_warning,
    has_compliance_after_warning,
)
from app.services.evaluator import evaluate
from app.services.messenger import send_warning
from app.utils.logger import log


WHITELIST = {
    "illegitimatehumans",
}


def process(user):

    username = user["username"]
    log.info(f"Processing {username}")

    if username in WHITELIST:
        log.info(f"{username}: Whitelisted")
        return

    cached = get_user(username)

    if (
        cached
        and user["seconds"] < GRACE_PERIOD
    ):
        log.info(
            f"{username}: Waiting for grace period "
            f"({user['seconds']} / {GRACE_PERIOD}s)"
        )
        return

    if (
        cached
        and cached["status"] in ("GOOD", "LEECHER", "UNKNOWN")
        and not needs_recheck(username)
    ):
        record_stat(
            event="database_cache_hit",
            username=username,
            status=cached["status"],
            files=cached["files"],
            directories=cached["directories"],
        )

        log.info(
            f"{username}: Cached {cached['status']} - skipping browse"
        )

        return

    log.info(f"{username}: Evaluating")

    result = evaluate(username)

    if result["status"] == "GOOD":

        warning_time = get_last_warning(username)

        if (
            warning_time is not None
            and not has_compliance_after_warning(
                username,
                warning_time,
            )
        ):
            compliance_time = datetime.utcnow()

            duration_minutes = int(
                (
                    compliance_time - warning_time
                ).total_seconds() / 60
            )

            record_stat(
                event="compliance_achieved",
                username=username,
                status="GOOD",
                files=result["files"],
                directories=result["directories"],
                duration_ms=duration_minutes * 60 * 1000,
            )

            log.info(
                f"{username}: Compliance achieved "
                f"{duration_minutes} minutes after warning"
            )

        save_user(
            username=username,
            status=result["status"],
            files=result["files"],
            directories=result["directories"],
            warned=False,
        )

        log.info(
            f"{username}: GOOD "
            f"({result['files']} files / "
            f"{result['directories']} dirs)"
        )

        return

    if result["status"] == "UNKNOWN":

        save_user(
            username=username,
            status=result["status"],
            files=result["files"],
            directories=result["directories"],
            warned=cached["warned"] if cached else False,
        )

        log.warning(f"{username}: Browse failed")

        return

    save_user(
        username=username,
        status=result["status"],
        files=result["files"],
        directories=result["directories"],
        warned=cached["warned"] if cached else False,
    )

    log.warning(
        f"{username}: LEECHER "
        f"({result['files']} files / "
        f"{result['directories']} dirs)"
    )

    if not already_warned(username):

        if send_warning(
            username,
            result["files"],
            result["directories"],
        ):

            record_stat(
                event="warning_sent",
                username=username,
                status=result["status"],
                files=result["files"],
                directories=result["directories"],
            )

            runtime_warned.add(username)
            mark_warned(username)

            log.warning("")
            log.warning("======================================================")
            log.warning("LEECHER WARNING SENT")
            log.warning(f"User        : {username}")
            log.warning(f"Files       : {result['files']}")
            log.warning(f"Directories : {result['directories']}")
            log.warning("Database    : Updated")
            log.warning("======================================================")
