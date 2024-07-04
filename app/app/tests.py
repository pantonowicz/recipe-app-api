"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTestCase(SimpleTestCase):
    """Test cases for Calc.py"""

    def test_add(self):
        """Test adding two numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract(self):
        """Test subtracting two numbers"""
        res = calc.subtract(6, 5)
        self.assertEqual(res, 1)
