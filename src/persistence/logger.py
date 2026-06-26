from __future__ import annotations
import json
import os
from datetime import datetime
from typing import Any


LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "logs", "operations.log.json")


class OperationLogger:
    def __init__(self, path: str = LOG_PATH) -> None:
        self._path = os.path.abspath(path)
        os.makedirs(os.path.dirname(self._path), exist_ok=True)
        if not os.path.exists(self._path):
            self._write([])

    def log(self, operation: str) -> None:
        data = self._read()
        data.append({
            "operation": operation,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        })
        self._write(data)

    def get_all(self) -> list:
        return self._read()

    def clear(self) -> None:
        self._write([])

    def _read(self) -> list:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _write(self, data: list) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
