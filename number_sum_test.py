import unittest
from number_sum import calculate_sum

class TestNumberSum(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(), 80)

if __name__ == "__main__":
    unittest.main()
