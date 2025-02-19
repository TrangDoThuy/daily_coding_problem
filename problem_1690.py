"""
This problem was asked by Facebook.

Boggle is a game played on a 4 x 4 grid of letters. 
The goal is to find as many words as possible 
that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. 
Given a game board and a dictionary of valid words, implement a Boggle solver.
"""

import unittest


def in_dictionary(board, word):

    if len(word) == 0:
        return True

    i = 0
    visited = []
    possible_visit = []

    for j in range(0, len(board)):
        for i in range(0, len(board[0])):
            pos = (i, j)

            if can_find(word, 0, board, [], pos):
                return True

    return False

def can_find(word, i, board, visited_list, pos):

    x, y = pos

    if word[i] == board[y][x]:

        if i == len(word) - 1:
            return True

        update_visited_list = visited_list + [(x, y)]
        neighbors = find_all_neighbors(board, (x, y))
        possible_visit = [i for i in neighbors if i not in visited_list]
        
        for pos in possible_visit:

            if can_find(word, i+1, board, update_visited_list, pos):
                return True

        return False
        
    else:
        return False

def find_all_neighbors(board, pos):

    x, y = pos
    del_x_list = [-1, 0, 1]
    del_y_list = [-1, 0, 1]
    neighbors = []

    for del_x in del_x_list:
        for del_y in del_y_list:

            if del_x == 0 and del_y == 0:
                continue
            
            x_new = x + del_x
            y_new = y + del_y

            if (0 <= y_new < len(board)) and (0 <= x_new < len(board[0])):
                neighbors.append((x_new, y_new))

    return neighbors



def find_words(board, dictionary):

    result = set()

    for word in dictionary:

        if in_dictionary(board, word):
            result.add(word)

    return result

class TestBoggleSolver(unittest.TestCase):

    def test_find_words_1(self):
        board = [
            ['a', 'p', 'p', 'l'],
            ['e', 'a', 'p', 'e'],
            ['p', 'l', 'e', 'a'],
            ['p', 'e', 'a', 'r']
        ]
        dictionary = {"apple", "banana", "orange", "grape", "pineapple", "pear", "peach", "plum"}
        found_words = find_words(board, dictionary)
        
        # Define the expected words that can be formed from the board
        expected_words = {"apple", "pear"}
        
        # Assert that the found words match the expected words
        self.assertEqual(found_words, expected_words)

    def test_find_words_2(self):
        board = [
            ['G', 'I', 'Z'],
            ['U', 'E', 'K'],
            ['Q', 'S', 'E']
        ]
        dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]

        found_words = find_words(board, dictionary)
        
        # Define the expected words that can be formed from the board
        expected_words = {"GEEKS", "QUIZ"}
        
        # Assert that the found words match the expected words
        self.assertEqual(found_words, expected_words)

    def test_no_words_found(self):
        # Define a board with no valid words
        empty_board = [
            ['x', 'y', 'z', 'w'],
            ['q', 'r', 's', 't'],
            ['u', 'v', 'w', 'x'],
            ['y', 'z', 'a', 'b']
        ]

        dictionary = {"apple", "banana", "orange", "grape", "pineapple", "pear", "peach", "plum"}
        
        # Call the solver to find words on the empty board
        found_words = find_words(empty_board, dictionary)
        
        # Assert that no words are found
        self.assertEqual(found_words, set())


    def test_edge_cases(self):
        # Test a board with a single valid word
        single_word_board = [
            ['a', 'p', 'p', 'l'],
            [' ', ' ', ' ', 'e'],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]
        dictionary = {"apple", "banana", "orange", "grape", "pineapple", "pear", "peach", "plum"}
        
        found_words = find_words(single_word_board, dictionary)
        self.assertEqual(found_words, {"apple"})
    

    def test_same_letter(self):
        # Test a board with all the same letters
        same_letters_board = [
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a']
        ]

        dictionary = ["a", "aa", "aaa", "aaaa"]
        
        found_words = find_words(same_letters_board, dictionary)
        self.assertEqual(found_words, {"a", "aa", "aaa", "aaaa"})


unittest.main()