from pathlib import Path
import shutil

from app.api.slskd import api
from app.config import MIN_FILES, MIN_DIRECTORIES
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

    message = (
        load_message()
        .replace("{username}", username)
        .replace("{files}", str(files))
        .replace("{directories}", str(directories))
        .replace("{min_files}", str(MIN_FILES))
        .replace("{min_directories}", str(MIN_DIRECTORIES))
    )

    log.info(f"Sending warning to {username}")

    return api.send_message(
        username,
        message,
    )
