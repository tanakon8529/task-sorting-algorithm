import unittest

# Discover and run all test modules
if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('.', pattern='*_test.py')
    testRunner = unittest.TextTestRunner()
    testRunner.run(tests)
