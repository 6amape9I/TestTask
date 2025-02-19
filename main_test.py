import pytest
import os

from custom_structure.Tree import TreeNode
from image_output import save, video_create
from main import find_worst_parent


class TestTreeNode:
    @pytest.fixture
    def sample_tree(self):
        pairs = [(1, 2), (1, 3), (2, 4), (2, 5)]
        return TreeNode(1).create_from_list(pairs)

    def test_tree_creation(self, sample_tree):
        assert sample_tree.value == 1
        assert [c.value for c in sample_tree.children] == [2, 3]

        node2 = sample_tree.search(2)
        assert [c.value for c in node2.children] == [4, 5]

    def test_node_deletion(self, sample_tree):
        sample_tree.delete(2)
        assert sample_tree.search(2) is None
        assert [c.value for c in sample_tree.children] == [3, 4, 5]

    def test_search_nonexistent(self, sample_tree):
        assert sample_tree.search(99) is None


class TestWorstParent:
    @pytest.fixture
    def trees(self):
        tree1 = TreeNode(1).create_from_list([(1, 2), (1, 3), (2, 4), (2, 5)])
        tree2 = TreeNode(1).create_from_list([(1, 2), (1, 3), (3, 4), (3, 5)])
        return tree1, tree2

    def test_find_worst_parent(self, trees):

        result = find_worst_parent(5, trees[0], trees[1])
        assert result == 2

    def test_no_worst_parent(self):
        tree1 = TreeNode(1).create_from_list([(1, 2)])
        tree2 = TreeNode(1).create_from_list([(1, 2)])
        assert find_worst_parent(2, tree1, tree2) is False


