import pytest
from src.core.bst import BST


class TestBST:
    def test_empty_tree(self):
        t = BST()
        assert t.is_empty()
        assert t.size() == 0
        assert t.root is None

    def test_insert_single(self):
        t = BST()
        t.insert(10)
        assert t.root is not None
        assert t.root.key == 10
        assert t.size() == 1

    def test_insert_multiple(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        t.insert(15)
        assert t.size() == 3
        assert t.root.left.key == 5
        assert t.root.right.key == 15

    def test_insert_duplicate(self):
        t = BST()
        t.insert(10)
        t.insert(10)
        assert t.size() == 1

    def test_search_found(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        t.insert(15)
        node = t.search(5)
        assert node is not None
        assert node.key == 5

    def test_search_not_found(self):
        t = BST()
        t.insert(10)
        assert t.search(99) is None

    def test_delete_leaf(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        assert t.delete(5) is True
        assert t.size() == 1
        assert t.search(5) is None

    def test_delete_node_with_one_child(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        t.insert(3)
        assert t.delete(5) is True
        assert t.size() == 2
        assert t.root.left.key == 3

    def test_delete_node_with_two_children(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        t.insert(15)
        t.insert(3)
        t.insert(7)
        assert t.delete(5) is True
        assert t.size() == 4
        assert t.root.left.key == 7

    def test_delete_root(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        t.insert(15)
        assert t.delete(10) is True
        assert t.size() == 2

    def test_delete_nonexistent(self):
        t = BST()
        t.insert(10)
        assert t.delete(99) is False
        assert t.size() == 1

    def test_inorder(self):
        t = BST()
        for v in [10, 5, 15, 3, 7]:
            t.insert(v)
        assert t.inorder() == [3, 5, 7, 10, 15]

    def test_preorder(self):
        t = BST()
        for v in [10, 5, 15, 3, 7]:
            t.insert(v)
        assert t.preorder() == [10, 5, 3, 7, 15]

    def test_postorder(self):
        t = BST()
        for v in [10, 5, 15, 3, 7]:
            t.insert(v)
        assert t.postorder() == [3, 7, 5, 15, 10]

    def test_clear(self):
        t = BST()
        t.insert(10)
        t.insert(5)
        t.clear()
        assert t.is_empty()
        assert t.size() == 0
        assert t.root is None
