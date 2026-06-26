from __future__ import annotations
import tkinter as tk
from typing import List, Any, Optional
from .base_drawer import BaseDrawer


class StackDrawer(BaseDrawer):
    CELL_W = 100
    CELL_H = 40
    PAD = 6
    MARGIN = 40

    def draw(
        self,
        items: List[Any],
        active_index: Optional[int] = None,
        label: str = "",
    ) -> None:
        self.clear()
        c = self.canvas
        cw = int(c["width"])
        ch = int(c["height"])

        if label:
            c.create_text(
                cw // 2, 20, text=label,
                fill=self.COLORS["label"], font=self.FONT_LABEL, anchor="n",
            )

        if not items:
            c.create_text(
                cw // 2, ch // 2, text="(empty)",
                fill=self.COLORS["label"], font=self.FONT, anchor="center",
            )
            return

        n = len(items)
        total_h = n * self.CELL_H + (n - 1) * self.PAD
        start_y = (ch - total_h) // 2 + 20
        x0 = cw // 2 - self.CELL_W // 2

        for i, val in enumerate(items):
            y0 = start_y + (n - 1 - i) * (self.CELL_H + self.PAD)
            y1 = y0 + self.CELL_H

            if i == active_index:
                fill = self.COLORS["node_active"]
            elif i in self._highlighted:
                fill = self.COLORS["node_found"]
            else:
                fill = self.COLORS["node"]

            c.create_rectangle(
                x0, y0, x0 + self.CELL_W, y1,
                fill=fill, outline=self.COLORS["edge"], width=2,
            )
            c.create_text(
                x0 + self.CELL_W // 2, (y0 + y1) // 2,
                text=str(val), fill=self.COLORS["text"], font=self.FONT,
            )
            c.create_text(
                x0 - 8, (y0 + y1) // 2,
                text=f"[{i}]", fill=self.COLORS["label"],
                font=self.FONT_LABEL, anchor="e",
            )

            if i == n - 1:
                c.create_text(
                    x0 + self.CELL_W + 12, (y0 + y1) // 2,
                    text="← top", fill=self.COLORS["node_active"],
                    font=self.FONT_LABEL, anchor="w",
                )
