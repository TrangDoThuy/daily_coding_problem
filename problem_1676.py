"""
This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""

import unittest

class MapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key, value):
        self.map[key] = value

    def sum(self, prefix):
        total = 0
        for key, value in self.map.items():
            if key.startswith(prefix):
                total += value
        return total

class TestMapSum(unittest.TestCase):
    def test_0(self):
        mapsum = MapSum()

        mapsum.insert("columnar", 3)
        self.assertEqual(3, mapsum.sum("col"))

        mapsum.insert("column", 2)
        self.assertEqual(5, mapsum.sum("col"))

unittest.main()