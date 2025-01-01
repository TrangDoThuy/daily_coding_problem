"""
This problem was asked by Oracle.

You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board. The only pieces on the board are the black king and various white pieces. Given this matrix, determine whether the king is in check.

For details on how each piece moves, see here.

For example, given the following matrix:

...K....
........
.B......
......P.
.......R
..N.....
........
.....Q..
You should return True, since the bishop is attacking the king diagonally.
"""

import unittest

def is_king_in_check(board):
    # find king position
    row_king, col_king = None, None
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 'K':
                row_king, col_king = i, j
                break
        if col_king != None:
            break 
    if row_king == None:
        return None
    # check

    for dx in range(-1,2):
        for dy in range(-1,2):
            if dx == 0 and dy == 0: continue
            x, y = col_king + dx, row_king + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if board[y][x] != '.':
                    if board[y][x] in ['B','Q'] and abs(dx) == abs(dy):
                        return True
                    if board[y][x] in ['R', 'Q'] and dx * dy == 0:
                        return True
                    if board[y][x] == 'N' and abs(x - col_king) + abs(y - row_king) == 3:
                        return True
                    if board[y][x] == 'P' and y - row_king == -1 and abs(x - col_king) == 1:
                        return True
                    break
                x += dx
                y += dy
    return False

class TestIsKingInCheck(unittest.TestCase):
    def test_bishop_threat(self):
        chess_board = [
            ['.', '.', '.', 'K', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 'B', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.'],
            ['.', '.', '.', '.', '.', '.', '.', 'R'],
            ['.', '.', 'N', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', 'Q', '.', '.']
        ]
        self.assertTrue(is_king_in_check(chess_board))

    def test_no_threat(self):
        chess_board = [
            ['.', '.', '.', 'K', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.'],
            ['.', '.', '.', '.', '.', '.', '.', 'R'],
            ['.', '.', 'N', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', 'Q', '.', '.']
        ]
        self.assertFalse(is_king_in_check(chess_board))

    def test_no_threat_2(self):
        chess_board = [
            ['.', '.', '.', 'K', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'P', '.'],
            ['.', '.', '.', 'P', '.', '.', '.', 'R'],
            ['.', '.', 'N', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', 'Q', '.', '.', '.', '.']
        ]
        self.assertFalse(is_king_in_check(chess_board))

if __name__ == '__main__':
    unittest.main()


