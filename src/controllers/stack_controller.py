from __future__ import annotations
import tkinter as tk
from src.controllers.base_controller import BaseController
from src.core.stack import Stack
from src.visualization.stack_drawer import StackDrawer


class StackController(BaseController):
    def __init__(self, canvas, controls, log_panel, status_bar) -> None:
        super().__init__(canvas, controls, log_panel, status_bar)
        self._stack = Stack()
        self._drawer = StackDrawer(canvas)
        self._active_idx: int | None = None

    def activate(self) -> None:
        self.controls.add_button("Push", self._push)
        self.controls.add_button("Pop", self._pop)
        self.controls.add_button("Peek", self._peek)
        self.controls.btn_undo.config(command=self._undo)
        self.controls.btn_clear.config(command=self._clear)
        self._redraw()

    def _push(self) -> None:
        val = self.controls.get_value()
        if not val:
            self.status_bar.set("Enter a value to push")
            return
        try:
            self._stack.push(val)
            self._record(
                f"push({val})",
                lambda: self._stack.pop(),
            )
            self._active_idx = self._stack.size() - 1
            self.controls.clear_entry()
            self._redraw()
        except OverflowError:
            self.status_bar.set("Stack is full!")

    def _pop(self) -> None:
        try:
            val = self._stack.pop()
            self._record(
                f"pop() → {val}",
                lambda v=val: self._stack.push(v),
            )
            self._active_idx = None
            self._redraw()
        except IndexError:
            self.status_bar.set("Stack is empty!")

    def _peek(self) -> None:
        try:
            val = self._stack.peek()
            self._active_idx = self._stack.size() - 1
            self.log_panel.add(f"peek() → {val}")
            self._redraw()
        except IndexError:
            self.status_bar.set("Stack is empty!")

    def _clear(self) -> None:
        old = self._stack.items
        self._stack.clear()
        self._history.clear()
        self._active_idx = None
        self.log_panel.add("clear()")
        self.log_panel.clear()
        self.controls.set_undo_state(False)
        self._redraw()
        self._update_status()

    def _redraw(self) -> None:
        self._drawer.clear()
        self._drawer.draw(self._stack.items, self._active_idx, label="Stack")
        self._update_status()

    def _update_status(self) -> None:
        self.status_bar.set(f"Stack | size: {self._stack.size()}")
