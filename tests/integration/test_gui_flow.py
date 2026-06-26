import pytest
from src.core.stack import Stack
from src.core.queue import Queue
from src.core.bst import BST


class TestFullFlow:
    def test_stack_lifecycle(self):
        s = Stack(max_size=5)
        for i in range(5):
            s.push(i)
        assert s.is_full()
        assert s.peek() == 4
        vals = [s.pop() for _ in range(5)]
        assert vals == [4, 3, 2, 1, 0]
        assert s.is_empty()

    def test_queue_lifecycle(self):
        q = Queue(max_size=5)
        for i in range(5):
            q.enqueue(i)
        assert q.is_full()
        assert q.front() == 0
        assert q.rear() == 4
        vals = [q.dequeue() for _ in range(5)]
        assert vals == [0, 1, 2, 3, 4]
        assert q.is_empty()

    def test_bst_lifecycle(self):
        t = BST()
        for v in [50, 30, 70, 20, 40, 60, 80]:
            t.insert(v)
        assert t.size() == 7
        assert t.inorder() == [20, 30, 40, 50, 60, 70, 80]
        assert t.search(40) is not None
        assert t.search(99) is None
        t.delete(30)
        assert t.size() == 6
        assert 30 not in t.inorder()
        t.clear()
        assert t.is_empty()
