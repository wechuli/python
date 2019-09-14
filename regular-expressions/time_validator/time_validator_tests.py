import unittest
from time_validator import is_valid_time


class TestFormNumberValidity(unittest.TestCase):
    def test_correctly_formatted_time(self):
        test_string = "10:45"
        self.assertTrue(is_valid_time(test_string))

    def test_time_with_one_digit_at_hour(self):
        test_string = "1:23"
        self.assertTrue(is_valid_time(test_string))

    def test_time_that_contains_dot_for_colon(self):
        test_string = "10.45"
        self.assertFalse(is_valid_time(test_string))

    def test_for_normal_number(self):
        test_string = "1999"
        self.assertFalse(is_valid_time(test_string))

    def test_for_additional_numbers_in_hour(self):
        test_string = "145:23"
        self.assertFalse(is_valid_time(test_string))


if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
