from __future__ import annotations
from typing import Any, List


class Stack:
    def __init__(self, max_size: int = 20) -> None:
        self._items: List[Any] = []
        self._max_size = max_size

    @property
    def items(self) -> List[Any]:
        return list(self._items)

    def push(self, value: Any) -> None:
        if self.is_full():
            raise OverflowError("Stack is full")
        self._items.append(value)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self._max_size

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()
