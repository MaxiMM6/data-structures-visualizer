from __future__ import annotations
import tkinter as tk
from typing import Optional, Any, Dict, List
from .base_drawer import BaseDrawer
from src.core.bst import BSTNode


class BSTDrawer(BaseDrawer):
    NODE_R = 22
    V_GAP = 60

    def draw(
        self,
        root: Optional[BSTNode],
        highlight: Optional[Any] = None,
        label: str = "",
    ) -> None:
        self.clear()
        c = self.canvas
        cw = int(c["width"])
        ch = int(c["height"])

        if label:
            c.create_text(
                cw // 2, 16, text=label,
                fill=self.COLORS["label"], font=self.FONT_LABEL, anchor="n",
            )

        if root is None:
            c.create_text(
                cw // 2, ch // 2, text="(empty)",
                fill=self.COLORS["label"], font=self.FONT, anchor="center",
            )
            return

        # Расставить порядковые номера через in-order обход
        positions: Dict[int, int] = {}
        counter = [0]
        self._assign_positions(root, positions, counter)

        # Вычислить x для каждого узла равномерно по ширине холста
        n = len(positions)
        margin = self.NODE_R + 10
        step = (cw - 2 * margin) / max(n - 1, 1)

        def node_x(node: BSTNode) -> int:
            return round(margin + positions[id(node)] * step)

        # Вертикальный шаг адаптируется под высоту холста
        depth = self._depth(root)
        start_y = 50
        v_step = min(self.V_GAP, (ch - start_y - 20) / max(depth, 1))

        self._draw_recursive(root, node_x, start_y, v_step, highlight)

    def _assign_positions(
        self,
        node: Optional[BSTNode],
        positions: Dict[int, int],
        counter: List[int],
    ) -> None:
        if node is None:
            return
        self._assign_positions(node.left, positions, counter)
        positions[id(node)] = counter[0]
        counter[0] += 1
        self._assign_positions(node.right, positions, counter)

    def _draw_recursive(
        self,
        node: Optional[BSTNode],
        node_x,
        y: int,
        v_step: float,
        highlight: Optional[Any],
    ) -> None:
        if node is None:
            return

        c = self.canvas
        r = self.NODE_R
        x = node_x(node)
        child_y = round(y + v_step)

        if node.left:
            lx = node_x(node.left)
            c.create_line(
                x, y + r, lx, child_y - r,
                fill=self.COLORS["edge"], width=2,
            )
            self._draw_recursive(node.left, node_x, child_y, v_step, highlight)

        if node.right:
            rx = node_x(node.right)
            c.create_line(
                x, y + r, rx, child_y - r,
                fill=self.COLORS["edge"], width=2,
            )
            self._draw_recursive(node.right, node_x, child_y, v_step, highlight)

        if node.key == highlight:
            fill = self.COLORS["node_active"]
        elif node.key in self._highlighted:
            fill = self.COLORS["node_found"]
        else:
            fill = self.COLORS["node"]

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
