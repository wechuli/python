from parsing_bytes_exercise import parse_bytes
import unittest


class TestForBytesInString(unittest.TestCase):
    def test_for_bytes_occuring_amongst_other_numbers(self):
        test_string = "11010101 101 323"
        self.assertEqual(parse_bytes(test_string), ['11010101'])

    def test_for_multiple_occuring_bytes(self):
        test_string = "my data is: 10101010 11100010"
        self.assertEqual(parse_bytes(test_string), ['10101010', '11100010'])

    def test_when_bytes_occur_in_string(self):
        test_string = "this is just a random string with no bytes"
        self.assertFalse(parse_bytes(test_string))


if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
