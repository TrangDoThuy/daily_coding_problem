import unittest

def is_safe(graph, coloring_vertices, color, current_vertex):
    for vertex in range(len(graph)):
        if graph[current_vertex][vertex] == 1 and coloring_vertices[vertex] == color:
            return False
    return True


def graph_coloring_util(graph, k, coloring_vertices, current_vertex):
    if current_vertex == len(graph):
        return True

    for color in range(1, k + 1):
        if is_safe(graph, coloring_vertices, color, current_vertex):
            coloring_vertices[current_vertex] = color
            if graph_coloring_util(graph, k, coloring_vertices, current_vertex + 1):
                return True
            else:
                # backtrack: remove the color if it doesnt lead to a solution
                coloring_vertices[current_vertex] = 0
    return False

def color_graph(graph, k):

    coloring_vertices = [0] * len(graph)
    return graph_coloring_util(graph, k, coloring_vertices, 0)

class TestColorGraph(unittest.TestCase):
    def test_1(self):
        graph = [
            [0, 1],
            [1, 0]
            ]
        k = 2
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_2(self):
        graph = [
            [0, 1],
            [1, 0]
            ]
        k = 1
        expected_result = False
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_3(self):
        graph = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
            ]
        k = 3
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_4(self):
        graph = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
            ]
        k = 2
        expected_result = False
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_5(self):
        graph = [
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
            ]
        k = 2
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_6(self):
        graph = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]
            ]
        k = 3
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_7(self):
        graph = [
            [0, 1, 1, 0, 0],
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0]
            ]
        k = 2
        expected_result = False
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_8(self):
        graph = [
                [0]
                ]
        k = 1
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_9(self):
        graph = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
                ]
        k = 1
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_10(self):
        graph = [
                [0, 1, 1, 1],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [1, 0, 1, 0]
                ]
        k = 2
        expected_result = False
        self.assertEqual(color_graph(graph, k), expected_result)

    def test_11(self):
        graph = [
                [0, 1, 1, 0, 0],
                [1, 0, 1, 1, 0],
                [1, 1, 0, 0, 1],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0]
                ]
        k = 3
        expected_result = True
        self.assertEqual(color_graph(graph, k), expected_result)


unittest.main()