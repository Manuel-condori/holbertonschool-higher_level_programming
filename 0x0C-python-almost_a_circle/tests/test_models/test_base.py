#!/usr/bin/python3
"""Unittest for Base class"""
from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """Runs tests for base.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b2 = Base()
        cls.b3 = Base(22)
        cls.b4 = Base(2.2)
        cls.b5 = Base("two")

    def test_00_create(self):
        """Tests the creation of a Base class"""

        self.assertTrue(self.b1)

    @classmethod
    def tearDownClass(cls):
        """Breaks down the testing environment"""
        pass

#if __name__ == '__main__':
 #   unittest.main()    
