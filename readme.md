# Task Sorting Algorithm Project

This project contains various tasks related to backend development, including user authentication, number calculations, prime number checks, sorting algorithms, promotion calculations, and project time estimations. It also includes a comprehensive set of tests to ensure the functionality of each task.

## Project Structure

```
task-sorting-algorithm/
│
├── change_calculator.py
├── change_calculator_test.py
│
├── employee_queries.py
├── employee_queries_test.py
│
├── number_sum.py
├── number_sum_test.py
│
├── prime_checker.py
├── prime_checker_test.py
│
├── prime_sum.py
├── prime_sum_test.py
│
├── project_time_calculator.py
├── project_time_calculator_test.py
│
├── promotion_calculator.py
├── promotion_calculator_test.py
│
├── sort_numbers.py
├── sort_numbers_test.py
│
├── user_auth.py
├── user_auth_test.py
│
├── run_tests.py
├── README.md
└── venv/
```

## Setting Up the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tanakon8529/task-sorting-algorithm.git
   cd task-sorting-algorithm
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have a `requirements.txt` file with the following content:
   ```txt
   unittest
   ```

## Running the Tests

To run all the tests, execute the `run_tests.py` script:

```bash
python run_tests.py
```

This will discover and run all test modules in the project.

## Details of Each Module

### Change Calculator
**File:** `change_calculator.py`
- Function to calculate change for a transaction using various denominations.

**Test:** `change_calculator_test.py`
- Test cases for change calculation functionality.

### Employee Queries
**File:** `employee_queries.py`
- SQL queries to manage and retrieve employee information.

**Test:** `employee_queries_test.py`
- Test cases for employee query functions.

### Number Sum
**File:** `number_sum.py`
- Function to calculate the sum of numbers from 1 to 10 with specific conditions.

**Test:** `number_sum_test.py`
- Test cases for number sum calculation.

### Prime Checker
**File:** `prime_checker.py`
- Function to check if a number is prime.

**Test:** `prime_checker_test.py`
- Test cases for prime checking functionality.

### Prime Sum
**File:** `prime_sum.py`
- Function to sum prime numbers up to a given value.

**Test:** `prime_sum_test.py`
- Test cases for summing prime numbers.

### Project Time Calculator
**File:** `project_time_calculator.py`
- Function to calculate the number of days needed to complete a project based on task complexity.

**Test:** `project_time_calculator_test.py`
- Test cases for project time calculation.

### Promotion Calculator
**File:** `promotion_calculator.py`
- Function to calculate product prices after applying promotions.

**Test:** `promotion_calculator_test.py`
- Test cases for promotion calculation functionality.

### Sorting Algorithm
**File:** `sort_numbers.py`
- Function to sort a list of numbers.

**Test:** `sort_numbers_test.py`
- Test cases for sorting functionality.

### User Authentication
**File:** `user_auth.py`
- Functions for user registration, login, and password reset with validation.

**Test:** `user_auth_test.py`
- Test cases for user authentication functionalities.
