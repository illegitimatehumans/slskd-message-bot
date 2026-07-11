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

    min_files, min_directories = api.get_leecher_thresholds()

    message = (
        load_message()
        .replace("{username}", username)
        .replace("{files}", str(files))
        .replace("{directories}", str(directories))
        .replace("{min_files}", str(min_files))
        .replace("{min_directories}", str(min_directories))
    )

    log.info(f"Sending warning to {username}")

    return api.send_message(
        username,
        message,
    )
