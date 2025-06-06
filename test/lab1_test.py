import unittest
from lab1 import zigzag
class TestZigzag(unittest.TestCase):
    
    def test_1(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        expected = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13,
                    14, 15, 20, 19, 18, 17, 16]
        self.assertEqual(zigzag(matrix), expected)


if __name__ == "__main__":
    unittest.main()