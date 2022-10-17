#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMAxInteger(unittest.TestCase):
    def test_equality(self):
        """Make sure the maximum value in the list
        is really what it says it is
        """
        the_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(the_list), 4)

    def test_astring(self):
        """Test a string"""
        string = "Hallo"
        self.assertEqual(max_integer(string), 'o')
    def test_list_strings(self):
        """Test a list of strings"""
        list_str = ["me", "him", "together"]
        self.assertEqual(max_integer(list_str), "together")

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.3, 3.4, 5.3, 40.34, 34.4]
        self.assertEqual(max_integer(floats), 40.34)

    def test_single_element(self):
        """Test only one element ot be in the list"""
        single_element = [10]
        self.assertEqual(max_integer(single_element), 10)

    def test_empty_list(self):
        """Test an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_empty_string(self):
        """Test an empty string"""
        empty_str = ""
        self.assertEqual(max_integer(empty_str), None)
    
    def test_integers_and_floats(self):
        """Test a list of combined integers and floats"""
        int_w_float = [12.3, 4, 5.3, 4.4, 65, -6]
        self.assertEqual(max_integer(int_w_float), 65)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

if __name__ == '__main__':
    unittest.main()
