#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset teh ID counter before each test"""
        Base._Base__nb_objects = 0

    def test_auto_assign_id(self):
        """Test Automatic id assignment"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)

class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        Base._Base__nb_objects = 0
        self.rect1 = Rectangle(10, 2)
        self.rect2 = Rectangle(2, 10, 2, 2, 100)

    def test_id(self):
        """Test the id attribute."""
        self.assertEqual(self.rect1.id, 1)
        self.assertEqual(self.rect2.id, 100)

    def test_width(self):
        """Test the width attribute."""
        self.assertEqual(self.rect1.width, 10)
        with self.assertRaises(TypeError):
            self.rect1.width = "10"
        with self.assertRaises(ValueError):
            self.rect1.width = -10

    def test_height(self):
        """Test the height attribute."""
        self.assertEqual(self.rect1.height, 2)
        with self.assertRaises(TypeError):
            self.rect1.height = "2"
        with self.assertRaises(ValueError):
            self.rect1.height = -2

    def test_x(self):
        """Test the x attribute."""
        self.assertEqual(self.rect2.x, 2)
        with self.assertRaises(TypeError):
            self.rect1.x = "2"
        with self.assertRaises(ValueError):
            self.rect1.x = -2

    def test_y(self):
        """Test the y attribute."""
        self.assertEqual(self.rect2.y, 2)
        with self.assertRaises(TypeError):
            self.rect1.y = "2"
        with self.assertRaises(ValueError):
            self.rect1.y = -2

    def test_area(self):
        """Test the area method."""
        self.assertEqual(self.rect1.area(), 20)
        self.assertEqual(self.rect2.area(), 20)

    def test_display(self):
        """Test the display method."""
        import io
        import sys
        output = io.StringIO()
        sys.stdout = output
        self.rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##########\n##########\n")

    def test_update(self):
        """Test the update method."""
        self.rect1.update(89)
        self.assertEqual(self.rect1.id, 89)
        self.rect1.update(89, 2)
        self.assertEqual(self.rect1.width, 2)
        self.rect1.update(89, 2, 3)
        self.assertEqual(self.rect1.height, 3)
        self.rect1.update(89, 2, 3, 4)
        self.assertEqual(self.rect1.x, 4)
        self.rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rect1.y, 5)

if __name__ == '__main__':
    unittest.main()
