from __future__ import annotations
from typing import Any, List


class Queue:
    def __init__(self, max_size: int = 20) -> None:
        self._items: List[Any] = []
        self._max_size = max_size

    @property
    def items(self) -> List[Any]:
        return list(self._items)

    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise OverflowError("Queue is full")
        self._items.append(value)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items.pop(0)

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]

    def rear(self) -> Any:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self._max_size

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()
