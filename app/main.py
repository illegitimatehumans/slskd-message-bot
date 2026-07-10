import time

from app.config import CHECK_INTERVAL
from app.services.monitor import get_active_users
from app.services.processor import process
from app.services.messenger import ensure_message

print()
print("=" * 70)
print("slskd-Message-Bot")
print("=" * 70)

ensure_message()

while True:

    try:

        users = get_active_users()

        print()
        print(f"Active uploads: {len(users)}")

        for user in users:

            process(user)

    except Exception as e:

        print(e)

    time.sleep(CHECK_INTERVAL)
