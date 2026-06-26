from __future__ import annotations
import tkinter as tk
from src.controllers.base_controller import BaseController
from src.core.bst import BST
from src.visualization.bst_drawer import BSTDrawer


class BSTController(BaseController):
    def __init__(self, canvas, controls, log_panel, status_bar) -> None:
        super().__init__(canvas, controls, log_panel, status_bar)
        self._bst = BST()
        self._drawer = BSTDrawer(canvas)
        self._highlight: int | None = None

    def activate(self) -> None:
        self.controls.add_button("Insert", self._insert)
        self.controls.add_button("Delete", self._delete)
        self.controls.add_button("Search", self._search)
        self.controls.add_button("In-order", self._inorder)
        self.controls.btn_undo.config(command=self._undo)
        self.controls.btn_clear.config(command=self._clear)
        self._redraw()

    def _insert(self) -> None:
        val_str = self.controls.get_value()
        if not val_str:
            self.status_bar.set("Enter a numeric value")
            return
        try:
            val = int(val_str)
        except ValueError:
            self.status_bar.set("Value must be an integer")
            return

        existing = self._bst.search(val) is not None
        self._bst.insert(val)
        self._record(
            f"insert({val})",
            lambda v=val: self._bst.delete(v),
        )
        self._highlight = val
        self.controls.clear_entry()
        self._redraw()

    def _delete(self) -> None:
        val_str = self.controls.get_value()
        if not val_str:
            self.status_bar.set("Enter a numeric value to delete")
            return
        try:
            val = int(val_str)
        except ValueError:
            self.status_bar.set("Value must be an integer")
            return

        if self._bst.search(val) is None:
            self.status_bar.set(f"Key {val} not found")
            return

        self._bst.delete(val)
        self._record(
            f"delete({val})",
            lambda v=val: self._bst.insert(v),
        )
        self._highlight = None
        self.controls.clear_entry()
        self._redraw()

    def _search(self) -> None:
        val_str = self.controls.get_value()
        if not val_str:
            self.status_bar.set("Enter a numeric value to search")
            return
        try:
            val = int(val_str)
        except ValueError:
            self.status_bar.set("Value must be an integer")
            return

        node = self._bst.search(val)
        if node:
            self._highlight = val
            self._drawer.highlight_nodes({val})
            self.log_panel.add(f"search({val}) → found")
        else:
            self._highlight = None
            self._drawer.clear_highlight()
            self.log_panel.add(f"search({val}) → not found")
            self.status_bar.set(f"Key {val} not found")
        self.controls.clear_entry()
        self._redraw()

    def _inorder(self) -> None:
        result = self._bst.inorder()
        self.log_panel.add(f"in-order: {result}")
        self.status_bar.set(f"In-order: {result}")

    def _clear(self) -> None:
        self._bst.clear()
        self._history.clear()
        self._highlight = None
        self._drawer.clear_highlight()
        self.log_panel.add("clear()")
        self.log_panel.clear()
        self.controls.set_undo_state(False)
        self._redraw()
        self._update_status()

    def _redraw(self) -> None:
        self._drawer.clear_highlight()
        if self._highlight is not None:
            self._drawer.highlight_nodes({self._highlight})
        self._drawer.draw(self._bst.root, label="BST")
        self._update_status()

    def _update_status(self) -> None:
        self.status_bar.set(f"BST | size: {self._bst.size()}")
