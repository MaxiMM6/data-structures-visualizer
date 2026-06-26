from __future__ import annotations
import tkinter as tk
from typing import Any, Callable, List, Tuple
from src.gui.controls import ControlsPanel
from src.gui.operation_log import OperationLog
from src.gui.status_bar import StatusBar
from src.persistence.logger import OperationLogger


class BaseController:
    def __init__(
        self,
        canvas: tk.Canvas,
        controls: ControlsPanel,
        log_panel: OperationLog,
        status_bar: StatusBar,
    ) -> None:
        self.canvas = canvas
        self.controls = controls
        self.log_panel = log_panel
        self.status_bar = status_bar
        self._history: List[Tuple[str, Callable, Tuple]] = []
        self._op_logger = OperationLogger()

    def activate(self) -> None:
        raise NotImplementedError

    def _redraw(self) -> None:
        raise NotImplementedError

    def _record(self, name: str, undo_fn: Callable, undo_args: tuple = ()) -> None:
        self._history.append((name, undo_fn, undo_args))
        self._op_logger.log(name)
        self.log_panel.add(name)
        self.controls.set_undo_state(len(self._history) > 0)
        self._update_status()

    def _undo(self) -> None:
        if not self._history:
            return
        name, undo_fn, undo_args = self._history.pop()
        undo_fn(*undo_args)
        self.log_panel.add(f"Undo: {name}")
        self.controls.set_undo_state(len(self._history) > 0)
        self._redraw()
        self._update_status()

    def _clear(self) -> None:
        raise NotImplementedError

    def _update_status(self) -> None:
        pass
