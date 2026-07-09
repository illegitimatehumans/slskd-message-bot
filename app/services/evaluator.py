from app.api.slskd import api
from app.config import MIN_FILES, MIN_DIRECTORIES
from app.utils.logger import log


def evaluate(username):
    """
    Browse a user and determine whether they meet
    OwlTV's sharing requirements.
    """

    browse = api.browse_user(username)

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
        files < MIN_FILES
        and
        directories < MIN_DIRECTORIES
    ):
        status = "LEECHER"
    else:
        status = "GOOD"

    return {
        "status": status,
        "files": files,
        "directories": directories
    }
