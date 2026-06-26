from __future__ import annotations
import tkinter as tk
from typing import Optional, Any, Set
from .base_drawer import BaseDrawer
from src.core.bst import BSTNode


class BSTDrawer(BaseDrawer):
    NODE_R = 22
    V_GAP = 60
    H_GAP_BASE = 120

    def draw(
        self,
        root: Optional[BSTNode],
        highlight: Optional[Any] = None,
        label: str = "",
    ) -> None:
        self.clear()
        c = self.canvas
        cw = int(c["width"])

        if label:
            c.create_text(
                cw // 2, 16, text=label,
                fill=self.COLORS["label"], font=self.FONT_LABEL, anchor="n",
            )

        if root is None:
            c.create_text(
                cw // 2, int(c["height"]) // 2, text="(empty)",
                fill=self.COLORS["label"], font=self.FONT, anchor="center",
            )
            return

        depth = self._depth(root)
        x_span = min(cw - 40, 2 ** depth * 30)
        start_x = cw // 2
        start_y = 50
        self._draw_node(root, start_x, start_y, x_span // 2, highlight)

    def _draw_node(
        self,
        node: Optional[BSTNode],
        x: int, y: int,
        h_gap: int,
        highlight: Optional[Any],
    ) -> None:
        if node is None:
            return

        c = self.canvas
        r = self.NODE_R

        if node.key == highlight:
            fill = self.COLORS["node_active"]
        elif node.key in self._highlighted:
            fill = self.COLORS["node_found"]
        else:
            fill = self.COLORS["node"]

        if node.left:
            lx = x - h_gap
            ly = y + self.V_GAP
            c.create_line(
                x, y + r, lx, ly - r,
                fill=self.COLORS["edge"], width=2,
            )
            self._draw_node(node.left, lx, ly, h_gap // 2, highlight)

        if node.right:
            rx = x + h_gap
            ry = y + self.V_GAP
            c.create_line(
                x, y + r, rx, ry - r,
                fill=self.COLORS["edge"], width=2,
            )
            self._draw_node(node.right, rx, ry, h_gap // 2, highlight)

        c.create_oval(
            x - r, y - r, x + r, y + r,
            fill=fill, outline=self.COLORS["edge"], width=2,
        )
        c.create_text(
            x, y, text=str(node.key),
            fill=self.COLORS["text"], font=self.FONT,
        )

    @staticmethod
    def _depth(node: Optional[BSTNode]) -> int:
        if node is None:
            return 0
        return 1 + max(BSTDrawer._depth(node.left), BSTDrawer._depth(node.right))
