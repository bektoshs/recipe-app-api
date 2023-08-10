"""
Sample test
"""

from django.test import SimpleTestCase
from .calc import add, subtract, even_or_odd


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """
        Test adding numbers together.
        :return:
        """
        res = add(5, 4)

        self.assertEqual(res, 9)

    def test_subtract_numbers(self):
        """
        Test to subtract numbers
        :return:
        """
        res = subtract(34, 34)

        self.assertEqual(res, 0)

    def test_even_odd_number(self):
        """
        Test funding even or odd
        :return:
        """
        res = even_or_odd(8, 0)

        self.assertEqual(res, True)
