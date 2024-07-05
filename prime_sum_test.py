import unittest
from prime_sum import sum_prime_numbers

class TestPrimeSum(unittest.TestCase):
    def test_sum_prime_numbers(self):
        self.assertEqual(sum_prime_numbers(4), 5)
        self.assertEqual(sum_prime_numbers(5), 10)
        self.assertEqual(sum_prime_numbers(15), 41)

if __name__ == "__main__":
    unittest.main()
