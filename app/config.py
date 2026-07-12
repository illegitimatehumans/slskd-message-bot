import os

SLSKD_URL = os.getenv("SLSKD_URL", "http://gluetun_slskd:5030")
SLSKD_API_KEY = os.getenv("SLSKD_API_KEY")

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "60"))
GRACE_PERIOD = int(os.getenv("GRACE_PERIOD", "120"))

BROWSE_RETRY_DELAYS = [
    int(delay)
    for delay in os.getenv(
        "BROWSE_RETRY_DELAYS",
        "2,5,10"
    ).split(",")
]

MIN_FILES = int(os.getenv("MIN_FILES", "1000"))
MIN_DIRECTORIES = int(os.getenv("MIN_DIRECTORIES", "20"))

DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"

DATABASE = "/app/data/warned.sqlite"

LOG_FILE = "/app/logs/slskd-bot.log"

GOOD_RECHECK_MINUTES = int(
    os.getenv("GOOD_RECHECK_MINUTES", 60)
)
