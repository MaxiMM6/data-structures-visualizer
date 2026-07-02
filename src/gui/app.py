from __future__ import annotations
import tkinter as tk
from tkinter import ttk
from src.gui.controls import ControlsPanel
from src.gui.operation_log import OperationLog
from src.gui.status_bar import StatusBar
from src.controllers.stack_controller import StackController
from src.controllers.queue_controller import QueueController
from src.controllers.bst_controller import BSTController


class App:
    TITLE = "Data Structures Visualizer (Жиляков М.Н. БИС-24-3)"
    WIDTH = 1100
    HEIGHT = 720

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title(self.TITLE)
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.configure(bg="#181825")
        self.root.resizable(True, True)

        self._build_ui()
        self._init_controllers()
        self._switch_structure("stack")

    def _build_ui(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#181825")
        style.configure("TLabel", background="#181825", foreground="#cdd6f4", font=("Consolas", 10))
        style.configure("TButton", background="#313244", foreground="#cdd6f4", font=("Consolas", 10), padding=6)
        style.map("TButton", background=[("active", "#45475a")])
        style.configure("TEntry", fieldbackground="#313244", foreground="#cdd6f4", font=("Consolas", 10))
        style.configure("TCombobox", fieldbackground="#313244", foreground="#cdd6f4", font=("Consolas", 10))

        top = ttk.Frame(self.root)
        top.pack(fill=tk.X, padx=8, pady=(8, 0))

        ttk.Label(top, text="Structure:").pack(side=tk.LEFT, padx=(0, 6))
        self._var_struct = tk.StringVar(value="stack")
        cb = ttk.Combobox(
            top, textvariable=self._var_struct,
            values=["stack", "queue", "bst"], state="readonly", width=10,
        )
        cb.pack(side=tk.LEFT)
        cb.bind("<<ComboboxSelected>>", self._on_structure_change)

        main = ttk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        left = ttk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(left, bg="#1e1e2e", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        right = ttk.Frame(main, width=300)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=(8, 0))
        right.pack_propagate(False)

        self.controls = ControlsPanel(right)
        self.controls.pack(fill=tk.X)

        self.log_panel = OperationLog(right)
        self.log_panel.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

        self.status_bar = StatusBar(self.root)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def _init_controllers(self) -> None:
        self._controllers = {
            "stack": StackController(self.canvas, self.controls, self.log_panel, self.status_bar),
            "queue": QueueController(self.canvas, self.controls, self.log_panel, self.status_bar),
            "bst": BSTController(self.canvas, self.controls, self.log_panel, self.status_bar),
        }

    def _on_structure_change(self, _event=None) -> None:
        self._switch_structure(self._var_struct.get())

    def _switch_structure(self, name: str) -> None:
        for w in self.controls.ops_frame.winfo_children():
            w.destroy()
        self._controllers[name].activate()
        self.status_bar.set(f"Selected: {name}")

    def run(self) -> None:
        self.root.mainloop()
