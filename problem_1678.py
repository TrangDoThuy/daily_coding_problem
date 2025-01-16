"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. 
Return the quotient as an integer, ignoring the remainder.
"""

import unittest

def simple_division(a, b):
    result = 0
    while a >= b:
        a -= b
        result += 1
    return result, a



def division(a, b):
    if a < b:
        return 0
    if len(str(a)) <= len(str(b)) + 1:
        result, remainder = simple_division(a, b)
        return result
    str_a = str(a) 
    str_b = str(b)

    sub_a = str_a[: len(str_b)]
    sub_result, sub_remainding = simple_division(int(sub_a), b)
    result = str(sub_result)
    remainding = str(sub_remainding)

    for i in range(len(str_b),len(str_a)):
        sub_a = remainding + str_a[i]
        sub_result, sub_remainding = simple_division(int(sub_a), b)

        result += str(sub_result)
        remainding = str(sub_remainding)
    
    return int(result)


class TestDivision(unittest.TestCase):
    def test_0(self):
        a = 10
        b = 2
        self.assertEqual(division(a, b), 5)

    def test_1(self):
        a = 100
        b = 2
        self.assertEqual(division(a, b), 50)

    def test_2(self):
        a = 10000000000000000
        b = 2
        self.assertEqual(division(a, b), 5000000000000000)

    def test_3(self):
        a = 20320
        b = 72
        self.assertNotEqual(division(a, b), 2050)

unittest.main()
