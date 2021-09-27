from unittest import TestCase
from functions_to_test import Calculator
import math

class TestAdd(TestCase):

    def test_add_1(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_add_2(self):
        self.assertNotEqual(Calculator.add(12, 4), 7)

    def test_sub_1(self):
        self.assertEqual(Calculator.subtract(6, 3), 3)

    def test_sub_2(self):
        self.assertNotEqual(Calculator.subtract(14, 8), 31)

    def test_miul_01(self):
        self.assertEqual(Calculator.multiply(4, 3), 12)

    def test_mul_02(self):
        self.assertNotEqual(Calculator.multiply(7, 5), 111)

    def test_div_01(self):
        self.assertEqual(Calculator.divide(100, 10), 10)

    def test_div_02(self):
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide(10, 0)
