import re

users_db = {}

def validate_email(email):
    # Basic email validation regex
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_phone(phone):
    # Basic phone validation (10 digits)
    return re.match(r"^\d{10}$", phone) is not None

def validate_password(password):
    # Password should be at least 6 characters long
    return len(password) >= 6

def validate_name(name):
    # Name should be non-empty and at most 50 characters
    return 0 < len(name) <= 50

def register(username, password, first_name="", last_name=""):
    if validate_email(username) or validate_phone(username):
        if validate_password(password) and validate_name(first_name) and validate_name(last_name):
            if username in users_db:
                return "User already exists"
            users_db[username] = {
                "password": password,
                "first_name": first_name,
                "last_name": last_name
            }
            return "Registration successful"
        return "Invalid input"
    return "Invalid username"

def login(username, password):
    if username in users_db and users_db[username]["password"] == password:
        return "Login successful"
    return "Invalid username or password"

def forget_password(username):
    if username in users_db:
        # Mockup logic to send OTP
        return "OTP sent to your email/phone"
    return "User not found"

if __name__ == "__main__":
    # Example usage
    print(register("test@example.com", "password123", "John", "Doe"))
    print(login("test@example.com", "password123"))
    print(forget_password("test@example.com"))
