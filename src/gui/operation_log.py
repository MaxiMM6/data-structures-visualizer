from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from typing import List


class OperationLog(ttk.Frame):
    MAX_DISPLAY = 100

    def __init__(self, master: tk.Widget) -> None:
        super().__init__(master)
        self._build()

    def _build(self) -> None:
        ttk.Label(self, text="Operation Log", font=("Consolas", 12, "bold")).pack(anchor="w", pady=(0, 4))
        self._listbox = tk.Listbox(
            self, bg="#1e1e2e", fg="#cdd6f4",
            font=("Consolas", 9), selectbackground="#45475a",
            highlightthickness=0, borderwidth=0,
        )
        self._listbox.pack(fill=tk.BOTH, expand=True)

    def add(self, text: str) -> None:
        self._listbox.insert(tk.END, text)
        if self._listbox.size() > self.MAX_DISPLAY:
            self._listbox.delete(0)
        self._listbox.see(tk.END)

    def remove_last(self) -> None:
        if self._listbox.size() > 0:
            self._listbox.delete(tk.END)

    def clear(self) -> None:
        self._listbox.delete(0, tk.END)
