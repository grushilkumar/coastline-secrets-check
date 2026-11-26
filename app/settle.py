"""Marks the day's card settlements as posted."""
import psycopg

from app.db import connection_settings


def post_settlements(day: str) -> int:
    with psycopg.connect(**connection_settings()) as conn:
        cur = conn.execute("UPDATE settlements SET status = 'POSTED' WHERE settle_day = %s AND status = 'READY'", (day,))
        return cur.rowcount
