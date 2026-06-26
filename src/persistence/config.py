from __future__ import annotations
import json
import os
from typing import Any


CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "config.json")

DEFAULTS = {
    "animation_speed": 500,
    "color_scheme": "dark",
}


class Config:
    def __init__(self, path: str = CONFIG_PATH) -> None:
        self._path = os.path.abspath(path)
        os.makedirs(os.path.dirname(self._path), exist_ok=True)
        if not os.path.exists(self._path):
            self._write(DEFAULTS)

    def get(self, key: str, default: Any = None) -> Any:
        data = self._read()
        return data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        data = self._read()
        data[key] = value
        self._write(data)

    def _read(self) -> dict:
        with open(self._path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: dict) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
