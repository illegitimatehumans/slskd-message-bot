from app.api.slskd import api
from app.utils.logger import log


def evaluate(username):
    
    """
    Determine whether a user meets the configured sharing policy.
    """

    browse = api.browse_user(username)
    min_files, min_directories = api.get_leecher_thresholds()
    if browse is None:
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
