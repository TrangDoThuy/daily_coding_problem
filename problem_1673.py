"""
This problem was asked by Citrix.

You are given a circular lock with three wheels, each of which display the numbers 0 through 9 in order. 
Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends", 
meaning that if you turn the wheels to one of these combinations, 
the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit, in either direction. 
Given a lock initially set to 000, a target combination, and a list of dead ends, 
write a function that returns the minimum number of moves required to reach the target state, or None if this is impossible.
"""
import unittest

def neighbors(node):
    for i in range(len(node)):
        for change in [1, 9]:
            digit = int(node[i])
            changed_digit = (digit + change) % 10 
            yield node[:i] + str(changed_digit) + node[i+1:]
    

def minimum_moves(target, dead_ends):
    queue = [('000',0)]
    visited = ['000']
    while len(queue) > 0:
        node, depth = queue.pop(0)
        if node == target:       
            print(f"steps: {depth}")
            return depth     
        for neighbor in neighbors(node):
            if neighbor not in dead_ends and neighbor not in visited:
                visited.append(neighbor)
                queue.append((neighbor, depth+1))
    return None

class TestMinimumMoves(unittest.TestCase):
    def test_0(self):
        target = "111"
        dead_ends = ["222"]
        self.assertEqual(3, minimum_moves(target, dead_ends))

    def test_1(self):
        target = "002"
        dead_ends = ["102","902","012","092","001","003"]
        self.assertEqual(None, minimum_moves(target, dead_ends))

unittest.main()