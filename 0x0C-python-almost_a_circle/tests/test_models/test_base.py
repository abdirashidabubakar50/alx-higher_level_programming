#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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
        Base._Base__nb_objects = 0  # Reset the counter for Base class
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
            Rectangle("1", 2)  # width is not an integer
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)  # width is negative
        with self.assertRaises(ValueError):
            Rectangle(0, 2)  # width is zero

    def test_height(self):
        """Test the height attribute."""
        self.assertEqual(self.rect1.height, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")  # height is not an integer
        with self.assertRaises(ValueError):
            Rectangle(1, -2)  # height is negative
        with self.assertRaises(ValueError):
            Rectangle(1, 0)  # height is zero

    def test_x(self):
        """Test the x attribute."""
        self.assertEqual(self.rect2.x, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")  # x is not an integer
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)  # x is negative

    def test_y(self):
        """Test the y attribute."""
        self.assertEqual(self.rect2.y, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")  # y is not an integer
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)  # y is negative

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
        expected_output = "\n".join(["#" * 10 for _ in range(2)]) + "\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_display_with_xy(self):
        """Test the display method with x and y."""
        import io
        import sys
        output = io.StringIO()
        sys.stdout = output
        rect = Rectangle(2, 2, 2, 2)
        rect.display()
        sys.stdout = sys.__stdout__
        expected_output = "\n\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.rect1), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(self.rect2), "[Rectangle] (100) 2/2 - 2/10")

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

    def test_update_kwargs(self):
        """Test the update method with kwargs."""
        self.rect1.update(id=89, width=2, height=3, x=4, y=5)
        self.assertEqual(self.rect1.id, 89)
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.height, 3)
        self.assertEqual(self.rect1.x, 4)
        self.assertEqual(self.rect1.y, 5)


class TestSquare(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        Base._Base__nb_objects = 0  # Reset the counter for Base class
        self.square1 = Square(5)
        self.square2 = Square(3, 1, 2, 50)

    def test_initialization(self):
        """Test the initialization of the Square instance."""
        self.assertEqual(self.square1.id, 1)
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square1.y, 0)

        self.assertEqual(self.square2.id, 50)
        self.assertEqual(self.square2.size, 3)
        self.assertEqual(self.square2.x, 1)
        self.assertEqual(self.square2.y, 2)

    def test_size(self):
        """Test the size attribute."""
        self.assertEqual(self.square1.size, 5)
        self.assertEqual(self.square2.size, 3)

        with self.assertRaises(TypeError):
            self.square1.size = "10"  # size is not an integer

        with self.assertRaises(ValueError):
            self.square1.size = -10  # size is negative

        with self.assertRaises(ValueError):
            self.square1.size = 0  # size is zero

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.square1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(self.square2), "[Square] (50) 1/2 - 3")

    def test_update(self):
        """Test the update method."""
        self.square1.update(89)
        self.assertEqual(self.square1.id, 89)
        
        self.square1.update(89, 7)
        self.assertEqual(self.square1.size, 7)
        
        self.square1.update(89, 7, 8)
        self.assertEqual(self.square1.size, 7)  # size should be updated to 7
        
        self.square1.update(89, 7, 8, 9)
        self.assertEqual(self.square1.x, 9)
        
        self.square1.update(89, 7, 8, 9, 10)
        self.assertEqual(self.square1.y, 10)

    def test_update_kwargs(self):
        """Test the update method with kwargs."""
        self.square1.update(id=89, size=10, x=5, y=6)
        self.assertEqual(self.square1.id, 89)
        self.assertEqual(self.square1.size, 10)
        self.assertEqual(self.square1.x, 5)
        self.assertEqual(self.square1.y, 6)


if __name__ == '__main__':
    unittest.main()
