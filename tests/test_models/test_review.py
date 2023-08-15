#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):

    """Test Cases for the Review class."""

    def test_8_instantiation(self):
        """Tests instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))


if __name__ == "__main__":
    unittest.main()
