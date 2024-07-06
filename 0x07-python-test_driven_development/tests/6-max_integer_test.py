import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxinteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1,2,3,4,5]), 5)
    
    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    
    def test_mixed_integers(self):
        self.assertEqual(max_integer([-10, 0, 10, 20, -5]), 20)
    
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_all_same_elements(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
    
    def test_unsorted_list(self):
        self.assertEqual(max_integer([10, 1, 11, 3, 9]), 11)
    
    def test_list_with_zero(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
    
    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)
    
    def test_mixed_floats_and_integers(self):
        self.assertEqual(max_integer([1.1, 2, 3.3, 4, 5.5]), 5.5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000000, 2000000000, 3000000000]), 3000000000)

    def test_list_with_one_large_negative(self):
        self.assertEqual(max_integer([-1000000000, -2000000000, -3000000000]), -1000000000)

if __name__ == "__main__":
    unittest.main()
    