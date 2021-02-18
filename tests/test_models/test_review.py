#!/usr/bin/python3
"""
This module contains all tests for the Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class TestReviewAttributes(unittest.TestCase):
    """This class contains all tests for attribute value assignation."""
    def test_instanciation(self):
        """Test the creation of a Review instance."""
        inst1 = Review()
        self.assertIsInstance(inst1, Review)
        self.assertIsInstance(inst1, BaseModel)

    def test_unique_id(self):
        """Test the creation of different ids."""
        inst1 = Review()
        inst2 = Review()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_cross_attributes(self):
        """Test the usage of attributes from other classes."""
        inst1 = Review()
        place1 = Place()
        sokka = User()
        inst1.user_id = sokka.id
        inst1.place_id = place1.id
        self.assertIsInstance(inst1.user_id, str)
        self.assertIsInstance(inst1.place_id, str)
        self.assertEqual(inst1.user_id, sokka.id)
        self.assertEqual(inst1.place_id, place1.id)

    def test_to_dict_method(self):
        """Test method to_dict() and creation of instance with dict"""
        inst1 = Review()
        place1 = Place()
        sokka = User()
        inst1.user_id = sokka.id
        inst1.place_id = place1.id
        inst2 = Review(inst1.to_dict())
        self.assertEqual(inst1.user_id, inst2.user_id)
