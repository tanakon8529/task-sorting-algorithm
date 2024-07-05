import unittest
from project_time_calculator import calculate_project_time_with_levels

class TestProjectTimeCalculator(unittest.TestCase):
    def test_calculate_project_time_with_levels(self):
        tasks = {"Hard": 5, "Medium": 7, "Easy": 10}
        programmers = {"Senior": 2, "Junior": 5}
        self.assertEqual(calculate_project_time_with_levels(tasks, programmers), 6)

if __name__ == "__main__":
    unittest.main()
