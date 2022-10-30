#!/usr/bin/python3
""" Moduls for test base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest import TestCase


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
