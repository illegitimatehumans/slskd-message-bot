from pathlib import Path

from app.api.slskd import api
from app.utils.logger import log

MESSAGE_FILE = "/app/message.txt"


def load_message():

    return Path(MESSAGE_FILE).read_text(
        encoding="utf-8"
    )


def send_warning(username):

    message = load_message()

    log.info(f"Sending warning to {username}")

    return api.send_message(
        username,
        message
    )
