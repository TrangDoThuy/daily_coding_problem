"""
This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""

import unittest

class Node:
    def __init__(self, value):
        self.value  = value
        self.left   = None
        self.right  = None

def is_BST_Util(node, min, max):
    if node is None:
        return True
    if node.value < min or node.value > max:
        return False
    return is_BST_Util(node.left, min, node.value -1) and \
        is_BST_Util(node.right, node.value + 1, max)

def is_BST_tree(root):
    return is_BST_Util(root, float('-inf'), float('inf'))

def size_of_tree(root):
    if root is None:
        return 0
    return 1 + size_of_tree(root.left) + size_of_tree(root.right)

def largest_BST_Util(node):
    if node is None:
        return {
            "min": float('-inf'),
            "max": float('inf'),
            "size": 0
            }

    if node.left is None and node.right is None:
        return {
            "min": node.value,
            "max": node.value,
            "size": 1
            }
    left = largest_BST_Util(node.left)
    right = largest_BST_Util(node.right)

    # node is an BST "root"
    if left["max"] < node.value < right["min"]: 
        return {
            "min": left["min"],
            "max": right["max"],
            "size": left["size"] + 1 + right["size"]
        }
    return {
        "min": float('-inf'),
        "max": float('inf'),
        "size": max(left["size"], right["size"])
        }

def largest_BST(root):
    return largest_BST_Util(root)["size"]

class TestTreeIsBST(unittest.TestCase):
    def test_0(self):
            # Create a sample binary tree
            #      4
            #    /   \
            #   2     5
            #  / \
            # 1   3
        root = Node(4)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.left.right = Node(3)

        self.assertTrue(is_BST_tree(root))
        self.assertEqual(largest_BST(root), 5)

    def test_1(self):
        # Create a sample binary tree
        #      4
        #    /   \
        #   2     0
        #  / \
        # 1   3
        root = Node(4)
        root.left = Node(2)
        root.right = Node(0)
        root.left.left = Node(1)
        root.left.right = Node(3)

        self.assertFalse(is_BST_tree(root))
        self.assertEqual(largest_BST(root), 3)

unittest.main()



