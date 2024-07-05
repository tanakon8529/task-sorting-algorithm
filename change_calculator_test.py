import unittest
from change_calculator import calculate_change

class TestChangeCalculator(unittest.TestCase):
    def test_calculate_change(self):
        self.assertEqual(calculate_change(125, 200), {"Bank50": 1, "Bank20": 1, "Coin5": 1})

if __name__ == "__main__":
    unittest.main()
