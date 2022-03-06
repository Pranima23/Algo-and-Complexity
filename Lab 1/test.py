import unittest
from linear_search import linear_search
from binary_search import binary_search

class TestSearch(unittest.TestCase):

    def test_linear_search(self):
        
        values = [15, 2, 48, 56, 4, 6, 35]
        self.assertEqual(linear_search(values, 48), 2)
        self.assertEqual(linear_search(values, 2), 1)
        self.assertEqual(linear_search(values, 5), -1)

    def test_binary_search(self):

        values = [2, 4, 6, 15, 35, 48, 56]
        self.assertEqual(binary_search(values, 48), 5)
        self.assertEqual(binary_search(values, 2), 0)
        self.assertEqual(binary_search(values, 5), -1)

if __name__ == "__main__":
    unittest.main()