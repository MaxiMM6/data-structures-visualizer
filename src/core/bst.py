from __future__ import annotations
from typing import Any, List, Optional


class BSTNode:
    def __init__(self, key: Any) -> None:
        self.key = key
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BST:
    def __init__(self) -> None:
        self.root: Optional[BSTNode] = None
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, key: Any) -> BSTNode:
        node = BSTNode(key)
        if self.root is None:
            self.root = node
            self._size += 1
            return node
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = node
                    self._size += 1
                    return node
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = node
                    self._size += 1
                    return node
                current = current.right
            else:
                return current

    def search(self, key: Any) -> Optional[BSTNode]:
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, key: Any) -> bool:
        self.root, deleted = self._delete_recursive(self.root, key)
        if deleted:
            self._size -= 1
        return deleted

    def _delete_recursive(self, node: Optional[BSTNode], key: Any):
        if node is None:
            return None, False
        if key < node.key:
            node.left, deleted = self._delete_recursive(node.left, key)
            return node, deleted
        elif key > node.key:
            node.right, deleted = self._delete_recursive(node.right, key)
            return node, deleted
        else:
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
            else:
                successor = self._min_node(node.right)
                node.key = successor.key
                node.right, _ = self._delete_recursive(node.right, successor.key)
                return node, True

    @staticmethod
    def _min_node(node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self) -> List[Any]:
        result: List[Any] = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[BSTNode], result: List[Any]) -> None:
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def preorder(self) -> List[Any]:
        result: List[Any] = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[BSTNode], result: List[Any]) -> None:
        if node is not None:
            result.append(node.key)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self) -> List[Any]:
        result: List[Any] = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[BSTNode], result: List[Any]) -> None:
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.key)

    def clear(self) -> None:
        self.root = None
        self._size = 0
