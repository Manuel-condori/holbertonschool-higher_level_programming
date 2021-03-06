#!/usr/bin/python3
"""Unittest for Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle

import unittest
import io
import contextlib


class TestRectangle(unittest.TestCase):
    """Runs tests for rectangle.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base = _Base__nb_objects = 0
        cls.r1 = Rectangle(2, 3)
        cls.r2 = Rectangle(5, 5)
        cls.r3 = Rectangle(4, 5, 1)
        cls.r4 = Rectangle(6, 7, 1, 2, 98)
        cls.r5 = Rectangle(2, 5, 3, 4)


    def test_2_1_width(self):
        """Tests when integers are added for width"""

        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r3.width, 4)
        self.assertEqual(self.r4.width, 6)
        self.assertEqual(self.r5.width, 2)

    def test_2_2_height(self):
        """Tests when integers are added for width"""

        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r4.height, 7)
        self.assertEqual(self.r5.height, 5)

    def test_2_3_x(self):
        """Tests when integers are added for x"""

        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 1)
        self.assertEqual(self.r4.x, 1)
        self.assertEqual(self.r5.x, 3)

    def test_2_4_y(self):
        """Tests when integers are added for y"""

        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r4.y, 2)
        self.assertEqual(self.r5.y, 4)
    
    def test_3_0_width_error(self):
        """Tests for errors with width"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(2.2, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([2, 1], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({"hi": 3}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((3, 2), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(None, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(float('inf'), 1)

    def test_3_1_height_error(self):
        """Tests for errors with height"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 2.2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [2, 1])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, {"hi": 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (3, 2))
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, float('inf'))

    def test_3_2_x_error(self):
        """Tests for errors with x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, 2.2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, [2, 1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, {"hi": 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, (3, 2))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, float('inf'))

    def test_3_3_y_error(self):
        """Tests for errors with y"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, 2.2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, [2, 1])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, {"hi": 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, (3, 2))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -2)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, None)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, float('inf'))
    
    def test_4_0_area(self):
        """Tests the area method"""

        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r2.area(), 25)
        self.assertEqual(self.r3.area(), 20)
        self.assertEqual(self.r4.area(), 42)
        self.assertEqual(self.r5.area(), 10)

    def test_4_1_area_error(self):
        """Tests when area() should throw an error"""

        with self.assertRaises(TypeError):
            self.r1.area(1)
        with self.assertRaises(TypeError):
            self.r1.area("hi")
        with self.assertRaises(TypeError):
            self.r1.area({"hi: 1"})
        with self.assertRaises(TypeError):
            self.r1.area((1, 2))
        with self.assertRaises(TypeError):
            self.r1.area([1, 2])    
    
    def test_5_0_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r1.display()
        s = f.getvalue()
        self.assertEqual(s, "##\n##\n##\n")

    def test_5_1_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r2.display()
        s = f.getvalue()
        self.assertEqual(s, "#####\n#####\n#####\n#####\n#####\n")

    def test_6_0_str(self):
        """Tests the __str__ method"""

        self.assertEqual(Rectangle.__str__
                         (self.r1), "[Rectangle] (3) 0/0 - 2/3")
        self.assertEqual(Rectangle.__str__
                         (self.r2), "[Rectangle] (4) 0/0 - 5/5")
        self.assertEqual(Rectangle.__str__
                         (self.r3), "[Rectangle] (5) 1/0 - 4/5")
        self.assertEqual(Rectangle.__str__
                         (self.r4), "[Rectangle] (98) 1/2 - 6/7")
        self.assertEqual(Rectangle.__str__
                         (self.r5), "[Rectangle] (6) 3/4 - 2/5")
    
    def test_7_0_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r3.display()
        s = f.getvalue()
        self.assertEqual(s, " ####\n ####\n ####\n ####\n ####\n")

    def test_7_1_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r5.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n\n\n   ##\n   ##\n   ##\n   ##\n   ##\n")

    def test_8_0_update_args(self):
        """Tests the update function for *args"""

        r = Rectangle(4, 3, 1, 2, 98)
        r.update(22, 3, 4, 2, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 22)
    
    def test_9_0_update_kwargs(self):
        """Tests the update function for **kwargs"""

        r = Rectangle(4, 3, 1, 2, 98)
        r.update(x=10, height=30, y=20, width=40, id=8)
        self.assertEqual(r.width, 40)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 20)

    def test_9_1_update_kwargs_width(self):
        """Tests the update function for **kwargs for width"""

        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(width=20)
        self.assertEqual(r.width, 20)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 20/3")

    def test_9_2_update_kwargs_height(self):
        """Tests the update function for **kwargs for height"""

        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(height=1)
        self.assertEqual(r.height, 1)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/1")

    def test_9_3_update_kwargs_x(self):
        """Tests the update function for **kwargs for x"""

        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(x=15)
        self.assertEqual(r.x, 15)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 15/2 - 4/3")

    def test_9_3_update_kwargs_y(self):
        """Tests the update function for **kwargs for y"""

        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(y=20)
        self.assertEqual(r.y, 20)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/20 - 4/3")

    def test_9_3_update_kwargs_id(self):
        """Tests the update function for **kwargs for id"""

        r = Rectangle(4, 3, 1, 2, 98)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (98) 1/2 - 4/3")
        r.update(id=22)
        self.assertEqual(r.id, 22)
        self.assertEqual(Rectangle.__str__
                         (r), "[Rectangle] (22) 1/2 - 4/3")

    def test_9_4_update_width_with_non_ints(self):
        """Tests for when non-ints are passed to width"""

        with self.assertRaises(TypeError):
            self.r5.update(width="hi", height=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(width=2.2, height=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(width={"hi": 5}, height=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(width=[1, 2], height=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(width=(1, 2), height=9, x=7)

    def test_9_5_update_height_with_non_ints(self):
        """Tests for when non-ints are passed to height"""

        with self.assertRaises(TypeError):
            self.r5.update(height="hi", width=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(height=2.2, y=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(height={"hi": 5}, width=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(width=5, height=[1, 2], y=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(height=(1, 2), width=9, x=7)

    def test_9_6_update_x_with_non_ints(self):
        """Tests for when non-ints are passed to x"""

        with self.assertRaises(TypeError):
            self.r5.update(x="hi", width=9, y=7)
        with self.assertRaises(TypeError):
            self.r5.update(x=2.2, y=9, height=7)
        with self.assertRaises(TypeError):
            self.r5.update(x={"hi": 5}, width=9, y=7)
        with self.assertRaises(TypeError):
            self.r5.update(width=5, x=[1, 2], y=9)
        with self.assertRaises(TypeError):
            self.r5.update(x=(1, 2), width=9, y=7)

    def test_9_7_update_y_with_non_ints(self):
        """Tests for when non-ints are passed to y"""

        with self.assertRaises(TypeError):
            self.r5.update(y="hi", width=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(y=2.2, x=9, height=7)
        with self.assertRaises(TypeError):
            self.r5.update(y={"hi": 5}, width=9, x=7)
        with self.assertRaises(TypeError):
            self.r5.update(width=5, y=[1, 2], x=9)
        with self.assertRaises(TypeError):
            self.r5.update(y=(1, 2), width=9, x=7)

    @classmethod
    def tearDownClass(cls):
        """Breaks down the testing environment"""
    
        pass
