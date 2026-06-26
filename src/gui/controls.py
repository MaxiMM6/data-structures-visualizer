from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional


class ControlsPanel(ttk.Frame):
    def __init__(self, master: tk.Widget) -> None:
        super().__init__(master)
        self._build()

    def _build(self) -> None:
        ttk.Label(self, text="Operations", font=("Consolas", 12, "bold")).pack(anchor="w", pady=(0, 6))

        entry_frame = ttk.Frame(self)
        entry_frame.pack(fill=tk.X, pady=(0, 6))
        ttk.Label(entry_frame, text="Value:").pack(side=tk.LEFT)
        self.entry_value = ttk.Entry(entry_frame, width=12)
        self.entry_value.pack(side=tk.LEFT, padx=4)

        self.ops_frame = ttk.Frame(self)
        self.ops_frame.pack(fill=tk.X)

        self.btn_undo = ttk.Button(self, text="Undo", state=tk.DISABLED)
        self.btn_undo.pack(fill=tk.X, pady=(12, 0))

        self.btn_clear = ttk.Button(self, text="Clear All")
        self.btn_clear.pack(fill=tk.X, pady=(4, 0))

    def get_value(self) -> str:
        return self.entry_value.get().strip()

    def clear_entry(self) -> None:
        self.entry_value.delete(0, tk.END)

    def add_button(self, text: str, command: Callable) -> ttk.Button:
        btn = ttk.Button(self.ops_frame, text=text, command=command)
        btn.pack(fill=tk.X, pady=2)
        return btn

    def set_undo_state(self, enabled: bool) -> None:
        self.btn_undo.config(state=tk.NORMAL if enabled else tk.DISABLED)
