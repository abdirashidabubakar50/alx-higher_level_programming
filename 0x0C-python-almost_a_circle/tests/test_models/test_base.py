#!/usr/bin/python3
import unittest
Base = __import__('models/base.py').Base

class TestBase(unittest.TestCase):
    def setup(self):
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
        