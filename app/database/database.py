import sqlite3
from datetime import datetime, timedelta

from app.config import (
    DATABASE,
    GOOD_RECHECK_MINUTES,
    LEECHER_RECHECK_MINUTES,
    UNKNOWN_RECHECK_MINUTES,
)

conn = sqlite3.connect(DATABASE, check_same_thread=False)

# Current user state / cache
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

# Historical statistics/events
conn.execute("""
CREATE TABLE IF NOT EXISTS statistics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    event TEXT NOT NULL,
    status TEXT,
    files INTEGER,
    directories INTEGER,
    duration_ms INTEGER,
    created_at TEXT NOT NULL
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
    elif user["status"] == "UNKNOWN":
        interval = UNKNOWN_RECHECK_MINUTES
    else:
        interval = GOOD_RECHECK_MINUTES

    return (
        datetime.utcnow() - checked
        > timedelta(minutes=interval)
    )


def record_stat(
    event,
    username=None,
    status=None,
    files=None,
    directories=None,
    duration_ms=None,
):
    """
    Record a historical statistics event.
    """

    conn.execute(
        """
        INSERT INTO statistics
        (
            username,
            event,
            status,
            files,
            directories,
            duration_ms,
            created_at
        )
        VALUES
        (
            ?,
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
            event,
            status,
            files,
            directories,
            duration_ms,
            datetime.utcnow().isoformat(),
        ),
    )

    conn.commit()

def get_statistics_summary():
    """
    Return aggregate statistics from historical events.
    """

    summary = {}

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='evaluation'
        """
    )
    summary["users_evaluated"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='evaluation'
        AND status='GOOD'
        """
    )
    summary["good_users"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='evaluation'
        AND status='LEECHER'
        """
    )
    summary["leechers"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='evaluation'
        AND status='UNKNOWN'
        """
    )
    summary["unknown_evaluations"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='browse_success'
        """
    )
    summary["browse_successes"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='browse_failure'
        """
    )
    summary["browse_failures"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT AVG(duration_ms)
        FROM statistics
        WHERE event='evaluation'
        AND duration_ms IS NOT NULL
        """
    )
    average_duration = cur.fetchone()[0]
    summary["average_browse_duration_ms"] = (
        round(average_duration, 2)
        if average_duration is not None
        else 0
    )

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='warning_sent'
        """
    )
    summary["warnings_sent"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='session_cache_hit'
        """
    )
    summary["session_cache_hits"] = cur.fetchone()[0]

    cur = conn.execute(
        """
        SELECT COUNT(*)
        FROM statistics
        WHERE event='database_cache_hit'
        """
    )
    summary["database_cache_hits"] = cur.fetchone()[0]

    return summary
