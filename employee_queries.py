def query_hobbies_more_than_one():
    return """
    SELECT employee_id, COUNT(name) as hobby_count
    FROM employee_hobby
    GROUP BY employee_id
    HAVING hobby_count > 1;
    """

def query_high_salary():
    return """
    SELECT employee_id, name, lastname
    FROM employee
    WHERE salary >= 350;
    """

def query_high_efficiency_hobbies():
    return """
    SELECT hobby_name, COUNT(employee_id) as num_employees
    FROM employee
    JOIN employee_hobby ON employee.employee_id = employee_hobby.employee_id
    WHERE efficiency > 70
    GROUP BY hobby_name;
    """

def query_senior_employees():
    return """
    SELECT name, lastname
    FROM employee
    WHERE age > 25 AND efficiency > 80;
    """

if __name__ == "__main__":
    print(query_hobbies_more_than_one())
    print(query_high_salary())
    print(query_high_efficiency_hobbies())
    print(query_senior_employees())
