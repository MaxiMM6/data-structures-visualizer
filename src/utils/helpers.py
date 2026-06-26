from __future__ import annotations
from datetime import datetime


def validate_numeric_input(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def format_timestamp(dt: datetime | None = None) -> str:
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")
