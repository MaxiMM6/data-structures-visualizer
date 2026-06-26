from __future__ import annotations
import tkinter as tk
from src.controllers.base_controller import BaseController
from src.core.queue import Queue
from src.visualization.queue_drawer import QueueDrawer


class QueueController(BaseController):
    def __init__(self, canvas, controls, log_panel, status_bar) -> None:
        super().__init__(canvas, controls, log_panel, status_bar)
        self._queue = Queue()
        self._drawer = QueueDrawer(canvas)
        self._active_idx: int | None = None

    def activate(self) -> None:
        self.controls.add_button("Enqueue", self._enqueue)
        self.controls.add_button("Dequeue", self._dequeue)
        self.controls.add_button("Front", self._front)
        self.controls.btn_undo.config(command=self._undo)
        self.controls.btn_clear.config(command=self._clear)
        self._redraw()

    def _enqueue(self) -> None:
        val = self.controls.get_value()
        if not val:
            self.status_bar.set("Enter a value to enqueue")
            return
        try:
            self._queue.enqueue(val)
            self._record(
                f"enqueue({val})",
                lambda: self._queue.dequeue(),
            )
            self._active_idx = self._queue.size() - 1
            self.controls.clear_entry()
            self._redraw()
        except OverflowError:
            self.status_bar.set("Queue is full!")

    def _dequeue(self) -> None:
        try:
            val = self._queue.dequeue()
            self._record(
                f"dequeue() → {val}",
                lambda v=val: self._queue.enqueue(v),
            )
            self._active_idx = None
            self._redraw()
        except IndexError:
            self.status_bar.set("Queue is empty!")

    def _front(self) -> None:
        try:
            val = self._queue.front()
            self._active_idx = 0
            self.log_panel.add(f"front() → {val}")
            self._redraw()
        except IndexError:
            self.status_bar.set("Queue is empty!")

    def _clear(self) -> None:
        self._queue.clear()
        self._history.clear()
        self._active_idx = None
        self.log_panel.add("clear()")
        self.log_panel.clear()
        self.controls.set_undo_state(False)
        self._redraw()
        self._update_status()

    def _redraw(self) -> None:
        self._drawer.clear()
        self._drawer.draw(self._queue.items, self._active_idx, label="Queue")
        self._update_status()

    def _update_status(self) -> None:
        self.status_bar.set(f"Queue | size: {self._queue.size()}")
