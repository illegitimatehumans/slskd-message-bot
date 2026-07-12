from time import sleep

from app.api.slskd import api
from app.utils.logger import log


def evaluate(username):

    """
    Determine whether a user meets the configured sharing policy.
    """
    min_files, min_directories = api.get_leecher_thresholds()

    browse = None

    for attempt in range(1, 4):

        log.info(
            f"{username}: Browse attempt {attempt}/3"
        )

        browse = api.browse_user(username)

        if browse is not None:

         log.info(
             f"{username}: Browse succeeded on attempt {attempt}"
        )

        break

        if attempt < 3:

            log.warning(
                f"{username}: Browse attempt {attempt} failed, retrying in 3 seconds..."
            )

            sleep(3)

        if browse is None:

            log.warning(
                f"{username}: Browse failed after 3 attempts"
            )

        return {
            "status": "UNKNOWN",
            "files": 0,
            "directories": 0
        }

    files = 0

    for directory in browse["directories"]:
        files += directory.get("fileCount", 0)

    directories = browse.get("directoryCount", 0)

    if (
        files < min_files
        or
        directories < min_directories
    ):
        status = "LEECHER"
    else:
        status = "GOOD"

    return {
        "status": status,
        "files": files,
        "directories": directories
    }
