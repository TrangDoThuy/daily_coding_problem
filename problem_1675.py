"""
This problem was asked by Pandora.

Given an undirected graph, determine if it contains a cycle.
"""

import unittest 

def graph_has_cycle(graph):
    visited = set()
    node = list(graph.keys())[0]
    visited.add(node)
    queue = []
    queue.append((node, None))

    while queue:
        node, parent = queue.pop()

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, node))
                visited.add(neighbor)
            else:
                if neighbor != parent:
                    return True
    return False

class TestUndirectedGraphHasCycle(unittest.TestCase):
    def test_0(self):
        graph = {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3],
            3: [2, 4],
            4: [3]
        }
        self.assertTrue(graph_has_cycle(graph))

    def test_1(self):
        graph = {
            0: [1, 2],
            1: [0, 3, 5],
            2: [0, 4, 6],
            3: [1],
            4: [2],
            5: [1],
            6: [2]
        }
        self.assertFalse(graph_has_cycle(graph))
    def test_2(self):
        graph = {
            0: [1, 2],
            1: [0, 3, 5],
            2: [0, 4, 6],
            3: [1, 7],
            4: [2],
            5: [1],
            6: [2],
            7: [3]
        }
        self.assertFalse(graph_has_cycle(graph))

unittest.main()

