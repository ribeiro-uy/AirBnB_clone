#!/usr/bin/python3
"""This module contains all tests for the Amenity class."""
import unittest
from models.amenity import Amenity
import models
from datetime import datetime
from models.base_model import BaseModel


class TestAmenityAttributes(unittest.TestCase):
    """
    Test assignation of attributes to Amenity instance.
    Class attributes:
        name (str)
    """
    def test_correct_instantiation(self):
        """
        Create a new instance, check its type.
        """
        new_instance = Amenity()
        self.assertIsInstance(new_instance, Amenity)
        self.assertIsInstance(new_instance, BaseModel)

    def test_name(self):
        """
        Check the correct type of attribute name
        """
        new_instance = Amenity()
        new_instance.name = "lavo, plancho, cocino, cuido los guric"
        self.assertIsInstance(new_instance.name, str)
        second_instance = Amenity()
        second_instance.name = new_instance.name
        self.assertEqual(new_instance.name, second_instance.name)

    def test_unique_id(self):
        """
        Check the uniq uuid
        """
        my_amenity = Amenity()
        my_amenity2 = Amenity()
        self.assertNotEqual(my_amenity.id, my_amenity2)

    def test_dif_create_update_time(self):
        """Test that created_at and updated_at are different."""
        new_instance = Amenity()
        self.assertNotEqual(new_instance.created_at, new_instance.updated_at)

    def test_inherited_attributes(self):
        """Test types of inherited attributes."""
        new_instance = Amenity()
        self.assertIsInstance(new_instance.id, str)
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

    def test_inherited_method_to_dict(self):
        """Test functionality of inherited methods."""
        new_instance = Amenity()
        new_instance.name = "o sea jelouuu"
        new_dict = new_instance.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertEqual(new_dict["name"], new_instance.name)

    def test_creation_by_dictionary(self):
        """Create an instance passing it a dictionary."""
        inst1 = Amenity()
        inst1.name = "there is no war in ba sing se"
        inst2 = Amenity(inst1.to_dict())
        self.assertEqual(inst1.name, inst2.name)
