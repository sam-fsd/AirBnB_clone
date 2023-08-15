#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
import inspect
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    """Test cases for the City class"""

    def test_8_instantiation(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))
