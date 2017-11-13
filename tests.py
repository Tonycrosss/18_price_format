# TODO place your tests here
import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_string_number(self):
        pass

    def test_negative_numbers(self):
        pass

    def test_words(self):
        pass

    def test_empty_string(self):
        pass

    def test_float_number(self):
        pretty_num1 = format_price(32333245.25213321321)
        self.assertEqual(pretty_num1, '32 333 245')


if __name__ == '__main__':
    unittest.main()