import pytest
from src.core.queue import Queue


class TestQueue:
    def test_new_queue_is_empty(self):
        q = Queue()
        assert q.is_empty()
        assert q.size() == 0

    def test_enqueue(self):
        q = Queue()
        q.enqueue("a")
        assert not q.is_empty()
        assert q.size() == 1
        assert q.front() == "a"

    def test_enqueue_multiple(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.size() == 3
        assert q.front() == 1
        assert q.rear() == 3

    def test_dequeue(self):
        q = Queue()
        q.enqueue("x")
        q.enqueue("y")
        assert q.dequeue() == "x"
        assert q.dequeue() == "y"
        assert q.is_empty()

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_front_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.front()

    def test_rear_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.rear()

    def test_max_size(self):
        q = Queue(max_size=2)
        q.enqueue(1)
        q.enqueue(2)
        assert q.is_full()
        with pytest.raises(OverflowError):
            q.enqueue(3)

    def test_items_returns_copy(self):
        q = Queue()
        q.enqueue(1)
        items = q.items
        items.append(99)
        assert q.size() == 1

    def test_clear(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.clear()
        assert q.is_empty()
        assert q.size() == 0
