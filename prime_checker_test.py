import unittest
from prime_checker import check_number

class TestPrimeChecker(unittest.TestCase):
    def test_check_number(self):
        self.assertTrue(check_number(2))
        self.assertTrue(check_number(3))
        self.assertFalse(check_number(4))
        self.assertTrue(check_number(5))

if __name__ == "__main__":
    unittest.main()
