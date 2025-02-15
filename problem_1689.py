"""
This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""

import unittest
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def merge(list1, list2):
    print("-"*50)
    print("want to merge list1, list2: ")
    print_list(list1)
    print_list(list2)
    print("-"*50)

    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2

    print("-"*50)
    print("merged list: ")
    print_list(dummy.next)
    print("-"*50)
    return dummy.next

def sort(head):
    print("-"*50)
    print("want to sort: ")
    print_list(head)
    print("-"*50)
    if head is None or head.next is None:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
    list2 = slow.next
    slow.next = None

    return merge(sort(head), sort(list2))

def print_list(head):
    while head is not None:
        print(head.value, end=" ")
        head = head.next
    print()

class TestSortLinkedList(unittest.TestCase):
    def test_1(self):
        # create linked list 4 -> 1 -> -3 -> 99
        node3 = Node(99)
        node2 = Node(-3, node3)
        node1 = Node(1, node2)
        head  = Node(4, node1)

        print_list(head)

        head = sort(head)

        self.assertEqual(head.value, -3)
        self.assertEqual(head.next.value, 1)
        self.assertEqual(head.next.next.value, 4)
        self.assertEqual(head.next.next.next.value, 99)

    def test_empty_list(self):
        head = None
        sorted_head = sort(head)
        self.assertIsNone(sorted_head)

    def test_single_node(self):
        head = Node(5)
        sorted_head = sort(head)
        self.assertEqual(sorted_head.value, 5)
        self.assertIsNone(sorted_head.next)

    def test_two_nodes(self):
        # Test case: 2 -> 1 should become 1 -> 2
        node1 = Node(1)
        head = Node(2, node1)
        sorted_head = sort(head)

        self.assertEqual(sorted_head.value, 1)
        self.assertEqual(sorted_head.next.value, 2)
        self.assertIsNone(sorted_head.next.next)

unittest.main()