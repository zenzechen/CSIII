import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.testcase):
    
    def test_reverse_string(self):
        result = "hello"
        self.assertEqual(result, reverse_string("olleh"))
    def test_capitalize_string(self):
        result = "Hello"
        self.asserEqual(result, capitalize_string("hello"))
    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("hello"))

if __name__ == '__main__':