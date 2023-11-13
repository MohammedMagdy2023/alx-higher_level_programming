#!/usr/bin/python3
"""
This is test module for the rectangle models
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(4, 6, 2, 1, 12)

    def test_attributes(self):
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 1)
        self.assertEqual(self.r1.id, 12)

    def test_area(self):
        self.assertEqual(self.r1.area(), 24)

if __name__ == '__main__':
    unittest.main()
