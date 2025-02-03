"""
This problem was asked by Google.

Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid 
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them.
"""

import unittest

def count_min_remove_parentheses(input):
    n = len(input)
    stack = []
    num_remove = 0
    for i in range(n):
        if input[i] == '(':
            stack.append("(")
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                num_remove += 1
    num_remove += len(stack)
    return num_remove

class TestRemoveMinParentheses(unittest.TestCase):
    def test_0(self):
        input = "()())()"
        self.assertEqual(count_min_remove_parentheses(input),1)

    def test_1(self):
        input = ")("
        self.assertEqual(count_min_remove_parentheses(input),2)

unittest.main()

