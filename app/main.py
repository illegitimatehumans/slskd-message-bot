import time

from app.config import CHECK_INTERVAL
from app.services.monitor import get_active_users
from app.services.processor import process
from app.services.messenger import ensure_message
from app.api.slskd import SlskdAPI
from app.config import SLSKD_URL


print()
print("        ███████╗██╗     ███████╗██╗  ██╗██████╗")
print("        ██╔════╝██║     ██╔════╝██║ ██╔╝██╔══██╗")
print("        ███████╗██║     ███████╗█████╔╝ ██║  ██║")
print("        ╚════██║██║     ╚════██║██╔═██╗ ██║  ██║")
print("        ███████║███████╗███████║██║  ██╗██████╔╝")
print("        ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝")
print()
print("       ███╗   ███╗███████╗███████╗ █████╗  ██████╗ ███████╗")
print("       ████╗ ████║██╔════╝██╔════╝██╔══██╗██╔════╝ ██╔════╝")
print("       ██╔████╔██║█████╗  ███████╗███████║██║  ███╗█████╗")
print("       ██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║██║   ██║██╔══╝")
print("       ██║ ╚═╝ ██║███████╗███████║██║  ██║╚██████╔╝███████╗")
print("       ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝")
print()
print("                    ██████╗  ██████╗ ████████╗")
print("                    ██╔══██╗██╔═══██╗╚══██╔══╝")
print("                    ██████╔╝██║   ██║   ██║")
print("                    ██╔══██╗██║   ██║   ██║")
print("                    ██████╔╝╚██████╔╝   ██║")
print("                    ╚═════╝  ╚═════╝    ╚═╝")
print()
print("  slskd-Message-Bot")
print("  Automated sharing policy enforcement for slskd")
print()
print("  GitHub: https://github.com/illegitimatehumans/slskd-message-bot")
print("  License: MIT")
print()
print("=" * 70)

api = SlskdAPI()

try:
    application = api.get_application()

    print()
    print("  slskd connection:    CONNECTED")
    print(f"  Soulseek username:   {application.get('user', {}).get('username', 'unknown')}")
    print(f"  API:                 {SLSKD_URL}")
    print(f"  Check interval:      {CHECK_INTERVAL}s")
    print("  Statistics retention: 30 days")
    print()
    print("  Monitoring active uploads...")
    print()

except Exception as e:
    print()
    print(f"  slskd connection:    FAILED")
    print(f"  Error:                {e}")
    print()


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
