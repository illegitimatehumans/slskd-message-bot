from pathlib import Path
import shutil

from app.api.slskd import api
from app.utils.logger import log

DATA_DIR = Path("/app/data")

MESSAGE_FILE = DATA_DIR / "message.txt"

DEFAULT_MESSAGE = Path("/app/message.txt.example")


def ensure_message():

    DATA_DIR.mkdir(exist_ok=True)

    if MESSAGE_FILE.exists():
        return

    shutil.copy(DEFAULT_MESSAGE, MESSAGE_FILE)

    log.info("Created data/message.txt from message.txt.example")


def load_message():

    ensure_message()

    return MESSAGE_FILE.read_text(
        encoding="utf-8"
    ).strip()


def send_warning(username, files, directories):

    group = api.get_leecher_group()

    thresholds = group["thresholds"]

    upload = group["upload"]

    queued = upload["limits"]["queued"]

    daily = upload["limits"]["daily"]

    weekly = upload["limits"]["weekly"]

    placeholders = {
        "username": username,
        "files": files,
        "directories": directories,
        "min_files": thresholds["files"],
        "min_directories": thresholds["directories"],
        "upload_slots": upload["slots"],
        "speed_limit": upload["speedLimit"],
        "queue_files": queued["files"],
        "queue_size": queued["megabytes"],
        "daily_files": daily["files"],
        "daily_size": daily["megabytes"],
        "daily_failures": daily.get("failures"),
        "weekly_files": weekly["files"],
        "weekly_size": weekly["megabytes"],
        "weekly_failures": weekly.get("failures"),
    }

    message = load_message()

    for key, value in placeholders.items():

        message = message.replace(
            f"{{{key}}}",
            str(value)
        )

    log.info(f"Sending warning to {username}")

    return api.send_message(
        username,
        message,
    )
