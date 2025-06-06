import unittest
from lab7 import rabin_karp

class TestRabinKarp(unittest.TestCase):
    def test_rabin_karp_cases(self):
        test_cases = [
            ("hello world", "world", [6]),
            ("abababab", "ab", [0, 2, 4, 6]),
            ("hello", "world", []),
            ("abc", "", []),
            ("", "abc", []),
            ("short", "longerneedle", []),
            ("match", "match", [0]),
            ("aaaaa", "aaa", [0, 1, 2]),
        ]

        for haystack, needle, expected in test_cases:
            with self.subTest(haystack=haystack, needle=needle):
                self.assertEqual(rabin_karp(haystack, needle), expected)

if __name__ == "__main__":
    unittest.main()
