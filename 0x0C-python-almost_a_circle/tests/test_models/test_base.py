#!/usr/bin/python3
"""
This is test module for the base models
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing init Base class."""

    def test_id_n1(self):
        init1 = Base()
        init2 = Base()
        self.assertEqual(init1.id, init2.id - 1)

    def test_id_n2(self):
        init1 = Base()
        init2 = Base()
        init3 = Base()
        self.assertEqual(init1.id, init3.id - 2)
