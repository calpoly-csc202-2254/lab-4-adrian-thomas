import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import insert, lookup, delete, is_empty


class BSTTests(unittest.TestCase):

    def test_numeric_ordering(self):
        def comes_before(a: int, b: int) -> bool:
            return a < b

        tree = None
        for num in [10, 5, 15, 3, 7]:
            tree = insert(tree, num, comes_before)

        self.assertTrue(lookup(tree, 5, comes_before))
        self.assertTrue(lookup(tree, 10, comes_before))
        self.assertFalse(lookup(tree, 100, comes_before))

        tree = delete(tree, 5, comes_before)
        self.assertFalse(lookup(tree, 5, comes_before))

    def test_alphabetic_ordering(self):
        def comes_before(a: str, b: str) -> bool:
            return a < b

        tree = None
        for ch in ["m", "c", "r", "a", "z"]:
            tree = insert(tree, ch, comes_before)

        self.assertTrue(lookup(tree, "a", comes_before))
        self.assertFalse(lookup(tree, "x", comes_before))

        tree = delete(tree, "m", comes_before)
        self.assertFalse(lookup(tree, "m", comes_before))

    def test_euclidean_distance_from_origin(self):
        def comes_before(p1: Tuple[int, int], p2: Tuple[int, int]) -> bool:
            return (p1[0]**2 + p1[1]**2) < (p2[0]**2 + p2[1]**2)

        tree = None
        for pt in [(3, 4), (0, 0), (1, 1), (6, 8), (2, 2)]:
            tree = insert(tree, pt, comes_before)

        self.assertTrue(lookup(tree, (3, 4), comes_before))  # distance = 5
        self.assertTrue(lookup(tree, (0, 0), comes_before))  # distance = 0
        self.assertFalse(lookup(tree, (7, 7), comes_before))  # not inserted

        tree = delete(tree, (2, 2), comes_before)
        self.assertFalse(lookup(tree, (2, 2), comes_before))


if __name__ == '__main__':
    unittest.main()