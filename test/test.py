import unittest
from src.main import pairs_of_tribes


class TestCountDifferentPairs(unittest.TestCase):
    def test_count_different_pairs(self):
        pairs = [[3], [1, 2], [2, 4], [3, 5]]
        result = pairs_of_tribes(pairs)
        self.assertEqual(result, 4)

class TestCountDifferentPairs(unittest.TestCase):
    def test_count_different_pairs(self):
        pairs = [[3], [2, 4], [6, 8], [10, 12]]
        result = pairs_of_tribes(pairs)
        self.assertEqual(result, 0)

class TestCountDifferentPairs(unittest.TestCase):
    def test_count_different_pairs(self):
        pairs = [[3], [1, 2], [2, 3], [3, 4]]
        result = pairs_of_tribes(pairs)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
