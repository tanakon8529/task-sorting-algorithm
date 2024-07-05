import unittest
from employee_queries import query_hobbies_more_than_one, query_high_salary, query_high_efficiency_hobbies, query_senior_employees

class TestEmployeeQueries(unittest.TestCase):
    def test_queries(self):
        self.assertIn("HAVING hobby_count > 1", query_hobbies_more_than_one())
        self.assertIn("salary >= 350", query_high_salary())
        self.assertIn("efficiency > 70", query_high_efficiency_hobbies())
        self.assertIn("efficiency > 80", query_senior_employees())

if __name__ == "__main__":
    unittest.main()
