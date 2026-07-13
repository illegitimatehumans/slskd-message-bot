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

    log.info(f"Processing {username}")

    if username in WHITELIST:
        log.info(f"{username}: Whitelisted")
        return


    if username in runtime_warned:
        log.info(f"{username}: Already warned this runtime")
        return

    if already_warned(username):
        runtime_warned.add(username)
        log.info(f"{username}: Already warned previously")
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
        and cached["status"] in ("GOOD", "LEECHER")
        and not needs_recheck(username)
    ):
        log.info(f"{username}: Cached GOOD - skipping browse"

        )

        if cached["status"] == "LEECHER":
            log.info(
                f"{username}: Previously evaluated as a leecher"
            )
        return

    log.info(f"{username}: Evaluating")

    result = evaluate(username)

    save_user(
        username=username,
        status=result["status"],
        files=result["files"],
        directories=result["directories"],
        warned=False,
    )

    if result["status"] == "UNKNOWN":

        log.warning(f"{username}: Browse failed")

        return

    if result["status"] == "GOOD":

        log.info(
            f"{username}: GOOD "
            f"({result['files']} files / "
            f"{result['directories']} dirs)"
        )

        return

    log.warning(
        f"{username}: LEECHER "
        f"({result['files']} files / "
        f"{result['directories']} dirs)"
    )

    if send_warning(
        username,
        result["files"],
        result["directories"]
    ):

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
