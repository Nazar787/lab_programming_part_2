import unittest
import sys
import os

sys.path.append('../src')

from lab6 import build_graph, topological_sort

class TestTopologicalSort(unittest.TestCase):
    def test_example1(self):
        pairs = [
            ("visa", "foreignpassport"),
            ("visa", "hotel"),
            ("visa", "bankstatement"),
            ("bankstatement", "nationalpassport"),
            ("hotel", "creditcard"),
            ("creditcard", "nationalpassport"),
            ("nationalpassport", "birthcertificate"),
            ("foreignpassport", "nationalpassport"),
            ("foreignpassport", "militarycertificate"),
            ("militarycertificate", "nationalpassport"),
        ]
        graph, indegree, nodes = build_graph(pairs)
        result = topological_sort(graph, indegree, nodes)

       
        pos = {name: i for i, name in enumerate(result)}
        for a, b in pairs:
            self.assertLess(pos[b], pos[a])

    def test_example2(self):
        pairs = [("visa", "foreignpassport")]
        graph, indegree, nodes = build_graph(pairs)
        result = topological_sort(graph, indegree, nodes)
        self.assertEqual(result, ["foreignpassport", "visa"])

if __name__ == "__main__":
    unittest.main()
