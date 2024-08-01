import unittest
from models.square import Square


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