from app.services.runtime import runtime_warned
from app.config import GRACE_PERIOD
from app.database.database import (
    get_user,
    save_user,
    already_warned,
    mark_warned,
    needs_recheck,
)
from app.services.evaluator import evaluate
from app.services.messenger import send_warning
from app.utils.logger import log

WHITELIST = {
    "illegitimatehumans",
}


def process(user):

    username = user["username"]

    if username in WHITELIST:
        return

    if user["seconds"] < GRACE_PERIOD:
        return

    if username in runtime_warned:
        return

    if already_warned(username):
        runtime_warned.add(username)
        return

    cached = get_user(username)

    if (
        cached
        and cached["status"] == "GOOD"
        and not needs_recheck(username)
    ):
        return

    result = evaluate(username)

    if result["status"] == "UNKNOWN":
        log.warning(f"{username}: browse failed")
        return

    if result["status"] == "GOOD":

        save_user(
            username=username,
            status="GOOD",
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

    # User is below both thresholds (LEECHER)

    log.warning(
        f"{username}: LEECHER "
        f"({result['files']} files / "
        f"{result['directories']} dirs)"
    )

    if send_warning(username):

        runtime_warned.add(username)

        save_user(
            username=username,
            status="LEECHER",
            files=result["files"],
            directories=result["directories"],
            warned=True,
        )

        mark_warned(username)

        log.warning("")
        log.warning("========================================")
        log.warning("WARNING SENT")
        log.warning(f"User        : {username}")
        log.warning(f"Files       : {result['files']}")
        log.warning(f"Directories : {result['directories']}")
        log.warning("========================================")
