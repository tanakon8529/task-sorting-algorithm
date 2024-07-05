import unittest
from user_auth import register, login, forget_password, users_db

class TestUserAuth(unittest.TestCase):
    def setUp(self):
        users_db.clear()  # Clear the database before each test

    def test_register_success(self):
        result = register("test@example.com", "password123", "John", "Doe")
        self.assertEqual(result, "Registration successful")
        self.assertIn("test@example.com", users_db)

    def test_register_invalid_email(self):
        result = register("invalid-email", "password123", "John", "Doe")
        self.assertEqual(result, "Invalid username")

    def test_register_invalid_phone(self):
        result = register("12345", "password123", "John", "Doe")
        self.assertEqual(result, "Invalid username")

    def test_register_short_password(self):
        result = register("test@example.com", "pwd", "John", "Doe")
        self.assertEqual(result, "Invalid input")

    def test_register_long_first_name(self):
        long_name = "J" * 51
        result = register("test@example.com", "password123", long_name, "Doe")
        self.assertEqual(result, "Invalid input")

    def test_register_existing_user(self):
        register("test@example.com", "password123", "John", "Doe")
        result = register("test@example.com", "password123", "John", "Doe")
        self.assertEqual(result, "User already exists")

    def test_login_success(self):
        register("test@example.com", "password123", "John", "Doe")
        result = login("test@example.com", "password123")
        self.assertEqual(result, "Login successful")

    def test_login_invalid_username(self):
        result = login("nonexistent@example.com", "password123")
        self.assertEqual(result, "Invalid username or password")

    def test_login_invalid_password(self):
        register("test@example.com", "password123", "John", "Doe")
        result = login("test@example.com", "wrongpassword")
        self.assertEqual(result, "Invalid username or password")

    def test_forget_password_success(self):
        register("test@example.com", "password123", "John", "Doe")
        result = forget_password("test@example.com")
        self.assertEqual(result, "OTP sent to your email/phone")

    def test_forget_password_user_not_found(self):
        result = forget_password("nonexistent@example.com")
        self.assertEqual(result, "User not found")

if __name__ == "__main__":
    unittest.main()
