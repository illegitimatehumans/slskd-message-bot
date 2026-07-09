from datetime import datetime, timezone

from app.api.slskd import api
from app.utils.logger import log


def seconds_since(started_at: str) -> int:
    """
    Returns seconds since startedAt.
    """

    started = datetime.fromisoformat(
        started_at.replace("Z", "+00:00")
    )

    now = datetime.now(timezone.utc)

    return int((now - started).total_seconds())


def get_active_users():

    users = {}

    uploads = api.get_uploads()

    for upload in uploads:

        username = upload["username"]

        for directory in upload["directories"]:

            for file in directory["files"]:

                if file["state"] != "InProgress":
                    continue

                users[username] = {
                    "username": username,
                    "filename": file["filename"],
                    "started": file["startedAt"],
                    "seconds": seconds_since(file["startedAt"])
                }

    return list(users.values())
