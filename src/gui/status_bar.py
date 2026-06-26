from __future__ import annotations
import tkinter as tk
from tkinter import ttk


class StatusBar(ttk.Frame):
    def __init__(self, master: tk.Widget) -> None:
        super().__init__(master)
        self._label = ttk.Label(self, text="Ready", anchor="w")
        self._label.pack(fill=tk.X, padx=8, pady=4)

    def set(self, text: str) -> None:
        self._label.config(text=text)
