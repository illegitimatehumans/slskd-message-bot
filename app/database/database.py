import sqlite3
from datetime import datetime, timedelta

from app.config import (
    DATABASE,
    GOOD_RECHECK_MINUTES,
    LEECHER_RECHECK_MINUTES,
)

conn = sqlite3.connect(DATABASE, check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    status TEXT,
    files INTEGER,
    directories INTEGER,
    warned INTEGER DEFAULT 0,
    last_checked TEXT
)
""")

conn.commit()


def get_user(username):

    cur = conn.execute(
        """
        SELECT
            username,
            status,
            files,
            directories,
            warned,
            last_checked
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    row = cur.fetchone()

    if row is None:
        return None

    return {
        "username": row[0],
        "status": row[1],
        "files": row[2],
        "directories": row[3],
        "warned": bool(row[4]),
        "last_checked": row[5]
    }


def save_user(
    username,
    status,
    files,
    directories,
    warned=False
):

    conn.execute(
        """
        INSERT OR REPLACE INTO users
        (
            username,
            status,
            files,
            directories,
            warned,
            last_checked
        )
        VALUES
        (
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
        """,
        (
            username,
            status,
            files,
            directories,
            int(warned),
            datetime.utcnow().isoformat()
        )
    )

    conn.commit()


def already_warned(username):

    user = get_user(username)

    if user is None:
        return False

    return user["warned"]


def mark_warned(username):

    conn.execute(
        """
        UPDATE users
        SET
            warned=1,
            last_checked=?
        WHERE username=?
        """,
        (
            datetime.utcnow().isoformat(),
            username,
        ),
    )

    conn.commit()

def needs_recheck(username):

    user = get_user(username)

    if user is None:
        return True

    if user["last_checked"] is None:
        return True

    checked = datetime.fromisoformat(user["last_checked"])

    if user["status"] == "LEECHER":
        interval = LEECHER_RECHECK_MINUTES
    else:
        interval = GOOD_RECHECK_MINUTES

    return (
        datetime.utcnow() - checked
        > timedelta(minutes=interval)
    )
