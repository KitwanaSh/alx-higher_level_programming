#!/usr/bin/python3
""" Moduls for test base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
class TestBaseScen(unittest.TestCase):
    """ Test Base class """

    def setUp(self):
        """Invokes each test """
        Base.__nb_objects = 0

    def test_id(self):
        """ Test assined id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Default if tested """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attr """
        new = Base()
        new_2 = Base()
        new_3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new_2.id, 2)
        self.assertEqual(new_3.id, 3)

    def test_mixed_id(self):
        """ tesy nb obj attributes and assin it with id """
        new = Base()
        new_2 = Base(808)
        new_3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new_2.id, 808)
        self.assertEqual(new_3.id, 2)
