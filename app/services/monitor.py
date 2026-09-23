from datetime import datetime, timezone

from app.api.slskd import api


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
    """
    Return only users with at least one currently active upload.

    Users disappear automatically as soon as their uploads are no
    longer InProgress. Historical database/cache data is untouched.
    """

    users = {}

    uploads = api.get_uploads()

    for upload in uploads:
        username = upload["username"]

        for directory in upload.get("directories", []):
            for file in directory.get("files", []):

                # Only currently transferring uploads count.
                if file.get("state") != "InProgress":
                    continue

                users[username] = {
                    "username": username,
                    "filename": file["filename"],
                    "started": file["startedAt"],
                    "seconds": seconds_since(file["startedAt"]),
                }

                # One active file is enough to keep this user active.
                break

            if username in users:
                break

    return list(users.values())
