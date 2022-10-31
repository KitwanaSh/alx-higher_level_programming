#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest import TestCase
from unittest.mock import patch
from io import StringIO

class TestRectangleScen(unittest.TestCase):
    """ Test Rectangle class """

    def setUp(self):
        """ Method called for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """ Test new rect attributes """
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """ Test new rectangles """
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_the_Base_instance(self):
        """ Test rectangle is a base instance """
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amnt_attrs(self):
        """ Test Error Reaise with 1 arg passed """
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amnt_attrs_1(self):
        """ Test error raised iwth o args passed to it """
        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_valide_attrs(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """
        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)

    def test_area_2(self):
        """ Checking the return value of area method """
        new = Rectangle(2, 2)
        self.assertEqual(new.area(), 4)
        new.width = 5
        self.assertEqual(new.area(), 10)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_area_3(self):
        """ Checking the return value of area method """
        new = Rectangle(3, 8)
        self.assertEqual(new.area(), 24)
        new2 = Rectangle(10, 10)
        self.assertEqual(new2.area(), 100)

    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str_1(self):
        """ Test __str__ method returned ex """
        r1 = Rectangle(4, 6, 2, 4)
        retn= "[Rectangle] (1) 2/4 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), retn)

    def test_str_2(self):
        """ Test __str__ method returned ex """
        r1 = Rectangle(5, 3, 6, 7, 12)
        retn = "[Rectangle] (12) 6/7 - 5/3\n"
        with patch('sys.stdout', new = StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), retn)

        r1.id = 1
        r1.width = 20
        r1.height = 31
        retn = "[Rectangle] (1) 6/7 - 20/31\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), retn)

    def test_str_3(self):
        """ Test __str__ method returned ex """
        r1 = Rectangle(5, 10)
        retn = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), retn)

        r2 = Rectangle(22, 40, 3, 5)
        retn = "[Rectangle] (2) 3/5 - 22/40\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), retn)

        r3 = Rectangle(1, 1, 1, 1)
        retn = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), retn)

    def test_str_4(self):
        """ Test __str__ method returned """
        r1 = Rectangle(3, 3)
        retn = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), retn)

    def test_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        retn = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), retn)

    def test_display_4(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        retn = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), retn)

        r1.x = 4
        retn = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), retn)

        r1.y = 2
        retn = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), retn)
