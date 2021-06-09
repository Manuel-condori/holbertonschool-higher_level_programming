#!/usr/bin/python3
"""Unittest square"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

import unittest
import io
import contextlib

class TestSquare(unittest.TestCase):
    """Runs tests for square.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base = _Base__nb_objects = 0
        cls.s1 = Square(5)
        cls.s2 = Square(7)
        cls.s3 = Square(2, 2)
        cls.s4 = Square(3, 1, 2)

    def test_10_00_create(self):
        """Checks to see if the creation of a square was successful"""

        self.assertTrue(self.s1)
        self.assertTrue(self.s2)
        self.assertTrue(self.s3)
        self.assertTrue(self.s4)

    def test_10_01_subclass(self):
        """Checks if Square is a subclass of Rectangle and Base"""

        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_10_02_check_attrs(self):
        """Check if the attributes of Square are set appropriately"""

        self.assertEqual(self.s4.width, 3)
        self.assertEqual(self.s4.height, 3)
        self.assertEqual(self.s4.x, 1)
        self.assertEqual(self.s4.y, 2)

    def test_10_03_area(self):
        """Makes sure the area method works"""

        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 49)
        self.assertEqual(self.s3.area(), 4)
        self.assertEqual(self.s4.area(), 9)

    def test_10_04_display(self):
        """Makes sure the display method works"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.s4.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n ###\n ###\n ###\n")

    def test_10_05_str(self):
        """Tests the __str__ method"""

        self.assertEqual(Square.__str__
                         (self.s1), "[Square] (41) 0/0 - 5")
        self.assertEqual(Square.__str__
                         (self.s2), "[Square] (42) 0/0 - 7")
        self.assertEqual(Square.__str__
                         (self.s3), "[Square] (43) 2/0 - 2")
        self.assertEqual(Square.__str__
                         (self.s4), "[Square] (44) 1/2 - 3")

    def test_11_01_size_error(self):
        """Tests for errors with size"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(2.2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([2, 1])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square({"hi": 3})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square((3, 2))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-2)
        with self.assertRaises(TypeError):
            s = Square(None)
        with self.assertRaises(TypeError):
            s = Square(float('inf'))

    def test_11_02_size(self):
        """Checks the size method"""

        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s3.size, 2)
        self.assertEqual(self.s4.size, 3)    

    @classmethod
    def tearDownClass(cls):
        """Breaks down the testing environment"""

        pass
