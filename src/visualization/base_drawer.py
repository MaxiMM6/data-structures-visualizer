from __future__ import annotations
import tkinter as tk
from typing import Dict


class BaseDrawer:
    COLORS: Dict[str, str] = {
        "bg": "#1e1e2e",
        "node": "#89b4fa",
        "node_active": "#f9e2af",
        "node_deleted": "#f38ba8",
        "node_found": "#a6e3a1",
        "text": "#1e1e2e",
        "label": "#cdd6f4",
        "arrow": "#585b70",
        "edge": "#6c7086",
    }

    FONT = ("Consolas", 11)
    FONT_LABEL = ("Consolas", 10)

    def __init__(self, canvas: tk.Canvas) -> None:
        self.canvas = canvas
        self._highlighted = set()

    def clear(self) -> None:
        self.canvas.delete("all")

    def highlight_nodes(self, ids: set) -> None:
        self._highlighted = set(ids)

    def clear_highlight(self) -> None:
        self._highlighted.clear()
