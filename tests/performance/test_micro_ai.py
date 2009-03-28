#! /usr/bin/python2.5

"""Brief tests for micro_ai.py"""

__author__ = "collinwinter@google.com (Collin Winter)"

# Python imports
import unittest

# Local imports
import micro_ai


class MicroAiTests(unittest.TestCase):

    def test_permutations(self):
        result = set(micro_ai.permutations(range(3), 2))
        correct = set([(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)])
        self.assertEqual(result, correct)

    def test_alphametics(self):
        result = set(micro_ai.alphametics("ABAB + BABA == CCCC"))
        self.assertTrue("2727 + 7272 == 9999" in result, result)

    def test_n_queens(self):
        result = set(micro_ai.n_queens(4))
        correct = set([(1, 3, 0, 2), (2, 0, 3, 1)])
        self.assertEqual(result, correct)

if __name__ == "__main__":
    unittest.main()
