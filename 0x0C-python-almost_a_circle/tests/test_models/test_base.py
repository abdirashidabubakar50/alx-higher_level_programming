#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def setUp(self):
        """Reset the counter before each test"""
        Base._Base__nb_objects = 0
    
    def test_auto_assign_id(self):
        """Test Automatic id assignment"""
        instance1 = Base()
        instance2 = Base()
        instance3 = Base()
        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 2)
        self.assertEqual(instance3.id, 3)

if __name__ == '__main__':
    unittest.main()