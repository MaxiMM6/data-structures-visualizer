import pytest
from unittest.mock import MagicMock
from src.core.stack import Stack
from src.controllers.stack_controller import StackController


class TestStackControllerIntegration:
    def _make_controller(self):
        canvas = MagicMock()
        canvas.__getitem__ = lambda self, key: {"width": "800", "height": "600"}[key]
        controls = MagicMock()
        controls.get_value.return_value = "42"
        controls.ops_frame = MagicMock()
        controls.ops_frame.winfo_children.return_value = []
        log_panel = MagicMock()
        status_bar = MagicMock()
        return StackController(canvas, controls, log_panel, status_bar)

    def test_push_and_undo(self):
        ctrl = self._make_controller()
        ctrl._push()
        assert ctrl._stack.size() == 1
        ctrl._undo()
        assert ctrl._stack.size() == 0

    def test_push_pop_flow(self):
        ctrl = self._make_controller()
        ctrl._push()
        ctrl.controls.get_value.return_value = "99"
        ctrl._push()
        assert ctrl._stack.size() == 2
        ctrl._pop()
        assert ctrl._stack.size() == 1
        assert ctrl._stack.peek() == "42"

    def test_clear_resets(self):
        ctrl = self._make_controller()
        ctrl._push()
        ctrl._clear()
        assert ctrl._stack.is_empty()
        assert ctrl._history == []
