# TODO place your tests here
import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_string_number(self):
        pretty_num1 = format_price('14421412')
        self.assertEqual(pretty_num1, '14 421 412')

    def test_negative_numbers(self):
        pretty_num1 = format_price('-14421412')
        self.assertEqual(pretty_num1, '-14 421 412')

    def test_words(self):
        pretty_num1 = format_price('abracadabra')
        self.assertEqual(pretty_num1, pretty_num1)

    def test_empty_string(self):
        pretty_num1 = format_price('')
        self.assertEqual(pretty_num1, pretty_num1)

    def test_float_number(self):
        pretty_num1 = format_price(32333245.25213321321)
        self.assertEqual(pretty_num1, pretty_num1)


if __name__ == '__main__':
    unittest.main()