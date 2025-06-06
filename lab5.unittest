import unittest
from lab5 import parse_input, bfs_shortest_path

class TestBFSMaze(unittest.TestCase):
    def test_reachable_path(self):
        data = """0,0
7,5
10,10
1 1 1 1 1 0 0 1 0 1
0 1 1 1 1 1 0 1 1 1
0 0 1 0 1 1 1 0 1 0
1 0 1 1 0 1 0 1 0 0
0 0 1 0 0 1 0 1 0 0
0 1 1 0 1 0 0 1 0 0
0 0 0 1 0 0 1 0 0 0
1 1 0 0 1 1 0 0 0 0
1 1 1 1 0 0 1 0 0 1
0 0 1 0 0 1 0 1 0 1"""
        start, end, rows, cols, matrix = parse_input(data)
        result = bfs_shortest_path(start, end, rows, cols, matrix)
        self.assertEqual(result, -1)  

    def test_unreachable_start(self):
        data = """1,1
2,2
3,3
0 0 0
0 0 0
0 0 0"""
        start, end, rows, cols, matrix = parse_input(data)
        result = bfs_shortest_path(start, end, rows, cols, matrix)
        self.assertEqual(result, -1)

    def test_simple_case(self):
        data = """0,0
1,1
2,2
1 1
1 1"""
        start, end, rows, cols, matrix = parse_input(data)
        result = bfs_shortest_path(start, end, rows, cols, matrix)
        self.assertEqual(result, 2)  # (0,0) → (0,1) → (1,1)

if __name__ == "__main__":
    unittest.main()
