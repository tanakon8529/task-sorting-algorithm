import unittest
from sort_numbers import sort_numbers

class TestSortNumbers(unittest.TestCase):
    def test_sort_numbers(self):
        self.assertEqual(sort_numbers([10, 5, 11, 20, 4, 8]), [4, 5, 8, 10, 11, 20])

if __name__ == "__main__":
    unittest.main()
