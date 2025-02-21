import pytest
import os

from custom_structure.Tree import TreeNode
from graph_main import graph_main
from image_output import save, video_create
from main import find_worst_parent
from not_greedy_main import not_greedy_main


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

class TestMain():
    def test_main(self):
        first_tree_pairs = [(1, 2), (1, 4), (1, 7), (2, 12), (2, 3),
                            (3, 10), (4, 11), (4, 5), (4, 14),
                            (5, 9), (5, 15), (7, 8), (7, 6),
                            (8, 13)]
        second_tree_pairs = [(1, 6), (1, 2), (1, 13), (1, 7),
                             (6, 3), (3, 4), (3, 5),
                             (2, 11), (2, 8), (13, 12),
                             (13, 15), (13, 10),
                             (7, 14), (14, 9)]
        m_nodes = 15

        assert graph_main(m_nodes, first_tree_pairs, second_tree_pairs), 8

    def test_not_greed_main(self):
        first_tree_pairs = [(1, 2), (1, 4), (1, 7), (2, 12), (2, 3),
                            (3, 10), (4, 11), (4, 5), (4, 14),
                            (5, 9), (5, 15), (7, 8), (7, 6),
                            (8, 13)]
        second_tree_pairs = [(1, 6), (1, 2), (1, 13), (1, 7),
                             (6, 3), (3, 4), (3, 5),
                             (2, 11), (2, 8), (13, 12),
                             (13, 15), (13, 10),
                             (7, 14), (14, 9)]
        m_nodes = 15

        assert not_greedy_main(m_nodes, first_tree_pairs, second_tree_pairs), 7

    def test_big_problem(self):
        first_tree_pairs = [(1, 2), (1, 2), (2, 4), (2, 5), (3, 6),
                            (3, 7), (4, 8), (4, 9), (5, 10), (5, 11),
                            (6, 12), (6, 13), (7, 14), (7, 15), (8, 16),
                            (8, 17), (9, 18), (9, 19), (10, 20), (10, 21),
                            (11, 22), (11, 23), (12, 24), (12, 25), (13, 26),
                            (13, 27), (14, 28), (14, 29), (15, 30)]
        second_tree_pairs = [(1, 2), (1, 2), (2, 4), (2, 5), (3, 6),
                            (3, 7), (4, 8), (4, 9), (7, 10), (5, 11),
                            (5, 12), (6, 13), (7, 14), (7, 15), (8, 16),
                            (8, 17), (9, 18), (9, 19), (10, 20), (10, 21),
                            (11, 22), (11, 23), (12, 24), (12, 25), (13, 26),
                            (13, 27), (14, 28), (12, 29), (15, 30)]
        m_nodes = 30

        assert graph_main(m_nodes, first_tree_pairs, second_tree_pairs), 8

    def test_simple(self):
        first_tree_pairs = [(1, 2), (2, 3), (3, 4), (4, 5)]
        second_tree_pairs = [(1, 2), (2, 3), (2, 4), (4, 5)]
        m_nodes = 5

        assert graph_main(m_nodes, first_tree_pairs, second_tree_pairs), 1
        assert not_greedy_main(m_nodes, first_tree_pairs, second_tree_pairs), 1

    def test_no_delete(self):
        first_tree_pairs = [(1, 2), (2, 3), (3, 4), (4, 5)]
        second_tree_pairs = [(1, 2), (2, 3), (2, 4), (4, 5)]
        m_nodes = 5

        assert graph_main(m_nodes, first_tree_pairs, second_tree_pairs), 0
        assert not_greedy_main(m_nodes, first_tree_pairs, second_tree_pairs), 0





