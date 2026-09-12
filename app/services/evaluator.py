from time import sleep, perf_counter

from app.api.slskd import api
from app.config import (
    BROWSE_RETRY_DELAYS,
)
from app.database.database import record_stat
from app.utils.logger import log


def evaluate(username):

    """
    Determine whether a user meets the configured sharing policy.
    """

    start_time = perf_counter()

    group = api.get_leecher_group()
    thresholds = group["thresholds"]
    min_files = thresholds["files"]
    min_directories = thresholds["directories"]

    browse = None
    max_attempts = len(BROWSE_RETRY_DELAYS) + 1
    browse_failures = 0

    for attempt in range(1, max_attempts + 1):

        log.info(
            f"{username}: Browse attempt {attempt}/{max_attempts}"
        )

        browse = api.browse_user(username)

        if browse is not None:

            if attempt > 1:
                log.info(
                    f"{username}: Browse succeeded on attempt {attempt}"
                )

            break

        browse_failures += 1

        if attempt < max_attempts:

            delay = BROWSE_RETRY_DELAYS[attempt - 1]

            log.warning(
                f"{username}: Browse attempt {attempt}/{max_attempts} failed, "
                f"retrying in {delay} seconds..."
            )

            sleep(delay)

    duration_ms = int(
        (perf_counter() - start_time) * 1000
    )

    if browse is None:

        log.warning(
            f"{username}: Browse failed after {max_attempts} attempts"
        )

        record_stat(
            event="evaluation",
            username=username,
            status="UNKNOWN",
            files=0,
            directories=0,
            duration_ms=duration_ms,
        )

        record_stat(
            event="browse_failure",
            username=username,
            status="UNKNOWN",
            duration_ms=duration_ms,
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

    record_stat(
        event="evaluation",
        username=username,
        status=status,
        files=files,
        directories=directories,
        duration_ms=duration_ms,
    )

    if browse_failures > 0:
        record_stat(
            event="browse_failure",
            username=username,
            status=status,
            files=files,
            directories=directories,
            duration_ms=duration_ms,
        )

    record_stat(
        event="browse_success",
        username=username,
        status=status,
        files=files,
        directories=directories,
        duration_ms=duration_ms,
    )

    return {
        "status": status,
        "files": files,
        "directories": directories
    }
