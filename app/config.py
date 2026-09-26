import os

SLSKD_URL = os.getenv("SLSKD_URL", "http://docker-wireguard-pia:5030")
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

DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"

DATABASE = "/app/data/warned.sqlite"

LOG_FILE = "/app/logs/slskd-bot.log"

GOOD_RECHECK_MINUTES = int(
    os.getenv("GOOD_RECHECK_MINUTES", 1440)
)
LEECHER_RECHECK_MINUTES = int(
    os.getenv("LEECHER_RECHECK_MINUTES", 20)
)
UNKNOWN_RECHECK_MINUTES = int(
    os.getenv("UNKNOWN_RECHECK_MINUTES", 10)
)
UNKNOWN_RECHECK_BACKOFF_MINUTES = [
    int(minutes)
    for minutes in os.getenv(
        "UNKNOWN_RECHECK_BACKOFF_MINUTES",
        "10,10,30,60,1440"
    ).split(",")
]
STATISTICS_RETENTION_DAYS = int(
    os.getenv("STATISTICS_RETENTION_DAYS", "30")
)
