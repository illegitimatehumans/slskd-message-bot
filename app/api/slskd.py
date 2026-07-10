import requests
from requests.exceptions import ReadTimeout, HTTPError

from app.config import (
    SLSKD_URL,
    SLSKD_API_KEY,
)

from app.utils.logger import log


class SlskdAPI:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "X-API-Key": SLSKD_API_KEY,
            "Content-Type": "application/json"
        })

    def get(self, endpoint):

        r = self.session.get(
            f"{SLSKD_URL}{endpoint}",
            timeout=20
        )

        r.raise_for_status()

        return r.json()

    def put(self, endpoint, body):

        r = self.session.put(
            f"{SLSKD_URL}{endpoint}",
            json=body,
            timeout=20
        )

        log.info(
            f"PUT {endpoint} -> HTTP {r.status_code}"
        )

        if r.text:
            log.info(f"Response: {r.text}")

        r.raise_for_status()

        return r

    def post(self, endpoint, body):

        r = self.session.post(
            f"{SLSKD_URL}{endpoint}",
            json=body,
            timeout=20
        )

        log.info(
            f"POST {endpoint} -> HTTP {r.status_code}"
        )

        if r.text:
            log.info(f"Response: {r.text}")

        r.raise_for_status()

        return r

    def get_application(self):

        return self.get("/api/v0/application")

    def get_uploads(self):

        return self.get("/api/v0/transfers/uploads")

    def browse_user(self, username):

        try:

            return self.get(
                f"/api/v0/users/{username}/browse"
            )

        except ReadTimeout:

            log.warning(
                f"{username}: Browse request timed out."
            )

            return None

        except HTTPError as e:

            log.warning(
                f"{username}: Browse HTTP error: {e}"
            )

            return None

        except Exception as e:

            log.warning(
                f"{username}: Browse failed: {e}"
            )

            return None

    def send_message(self, username, message):

        try:

            self.post(
                f"/api/v0/conversations/{username}",
                message
            )

            log.info(
                f"Sent message to {username}"
            )

            return True

        except Exception as e:

            log.error(
                f"Message failed to {username}: {e}"
            )

            return False


api = SlskdAPI()
