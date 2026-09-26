import time
last_stats_time = 0
STATS_INTERVAL = 3600

from app.config import (
    CHECK_INTERVAL,
    SLSKD_URL,
    SLSKD_API_KEY,
    STATISTICS_RETENTION_DAYS,
)

from app.api.slskd import SlskdAPI
from app.services.messenger import ensure_message
from app.services.monitor import get_active_users
from app.services.processor import process
from app.database.database import get_statistics_summary

print("=" * 70)
print()
print()
print("              ███████╗██╗     ███████╗██╗  ██╗██████╗")
print("              ██╔════╝██║     ██╔════╝██║ ██╔╝██╔══██╗")
print("              ███████╗██║     ███████╗█████╔╝ ██║  ██║")
print("              ╚════██║██║     ╚════██║██╔═██╗ ██║  ██║")
print("              ███████║███████╗███████║██║  ██╗██████╔╝")
print("              ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═════╝")
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
print()
print("=" * 70)

api = SlskdAPI()

try:

    application = api.get_application()

    print()

    print("  slskd connection:       CONNECTED")
    print(f"  Soulseek username:      {application.get('user', {}).get('username', 'unknown')}")
    print(f"  slskd API endpoint:     {SLSKD_URL}")
    print("  API authentication:     CONFIGURED" if SLSKD_API_KEY else "  API authentication:     NOT CONFIGURED")
    print(f"  Check interval:         {CHECK_INTERVAL}s")
    print(f"  Statistics retention:   {STATISTICS_RETENTION_DAYS} days")
    print()

    print("  Monitoring active uploads...")

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


        if time.time() - last_stats_time >= STATS_INTERVAL:
            summary = get_statistics_summary()

            print()
            print("===== COMPLIANCE STATISTICS =====")
            print(f"Warned users        : {summary['unique_warned_users']}")
            print(f"Compliant users     : {summary['unique_compliant_users']}")
            print(f"Compliance rate     : {summary['compliance_rate_pct']}%")
            print(f"Avg time to comply  : {summary['average_minutes_to_compliance']} minutes")
            print("=================================")

            last_stats_time = time.time()

    except Exception as e:

        print(e)

    time.sleep(CHECK_INTERVAL)
