"""
This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.


"""
import unittest
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    
def forward_traversal(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()

def backward_traversal(tail):
    current = tail
    while current is not None:
        print(current.value, end=" ")
        current = current.prev
    print()

def is_palindrome(head):
    if head is None:
        return True
    
    current = head
    # move current to tail
    while current.next is not None: 
        current = current.next 
    # print(f"head = {head.value}, current.value = {current.value}")

    while (head is not current) and (head.prev is not current):
        if head.value != current.value:
            return False
        head = head.next
        current = current.prev
        # print(f"head = {head.value}, current.value = {current.value}")
    return True 
        

class TestLinkedListPalindrome(unittest.TestCase):
    def test_0(self):
        head    = Node(1)
        second  = Node(4)
        third   = Node(3)
        forth   = Node(4)
        fifth   = Node(1)

        head.prev   = None
        head.next   = second
        second.prev = head
        second.next = third
        third.prev  = second
        third.next  = forth
        forth.prev  = third
        forth.next  = fifth
        fifth.prev  = forth
        fifth.next  = None

        forward_traversal(head)
        backward_traversal(fifth)

        self.assertTrue(is_palindrome(head))

    def test_1(self):
        head    = Node(1)
        second  = Node(4)
       
        head.prev   = None
        head.next   = second
        second.prev = head
        second.next = None
        
        forward_traversal(head)
        backward_traversal(second)

        self.assertFalse(is_palindrome(head))


unittest.main()



