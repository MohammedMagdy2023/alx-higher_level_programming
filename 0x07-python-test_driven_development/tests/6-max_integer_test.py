#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_list(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

if __name__ == '__main__':
    unittest.main()
