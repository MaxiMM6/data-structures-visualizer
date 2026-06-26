import pytest
from src.core.stack import Stack


class TestStack:
    def test_new_stack_is_empty(self):
        s = Stack()
        assert s.is_empty()
        assert s.size() == 0

    def test_push(self):
        s = Stack()
        s.push("a")
        assert not s.is_empty()
        assert s.size() == 1
        assert s.peek() == "a"

    def test_push_multiple(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.size() == 3
        assert s.peek() == 3

    def test_pop(self):
        s = Stack()
        s.push("x")
        s.push("y")
        assert s.pop() == "y"
        assert s.pop() == "x"
        assert s.is_empty()

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push(42)
        assert s.peek() == 42
        assert s.size() == 1

    def test_max_size(self):
        s = Stack(max_size=2)
        s.push(1)
        s.push(2)
        assert s.is_full()
        with pytest.raises(OverflowError):
            s.push(3)

    def test_items_returns_copy(self):
        s = Stack()
        s.push(1)
        items = s.items
        items.append(99)
        assert s.size() == 1

    def test_clear(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.clear()
        assert s.is_empty()
        assert s.size() == 0
