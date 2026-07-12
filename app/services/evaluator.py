from time import sleep

from app.api.slskd import api
from app.config import (
    BROWSE_RETRY_DELAYS,
)
from app.utils.logger import log


def evaluate(username):

    """
    Determine whether a user meets the configured sharing policy.
    """
    min_files, min_directories = api.get_leecher_thresholds()

    browse = None

    max_attempts = len(BROWSE_RETRY_DELAYS) + 1

    for attempt in range(1, max_attempts + 1):

        log.info(
            f"{username}: Browse attempt {attempt}/{max_attempts}"
        )

        browse = api.browse_user(username)

        if browse is not None:

         log.info(
             f"{username}: Browse succeeded on attempt {attempt}"
        )

        break

        if attempt < max_attempts:
            delay = BROWSE_RETY_DELAYS[ATTEMPT - 1]
            log.warning(
                f"{username}: Browse attempt {attempt}/{max_attempts} failed,"
                f"retrying in {delay} seconds..."
            )

            sleep(delay)

        if browse is None:

            log.warning(
                f"{username}: Browse failed after {max_attempts} attempts"
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
