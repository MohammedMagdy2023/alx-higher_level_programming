#!/usr/bin/python3
"""
This is test module for the rectangle models
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        self.r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 6)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 1)
        self.assertEqual(self.r1.id, 12)

    def test_area(self):
        self.r2 = Rectangle(40, 60, 2, 1, 12)
        self.assertEqual(self.r2.area(), 2400)

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

if __name__ == '__main__':
    unittest.main()
