#!/usr/bin/python3
"""This module contains all tests for the City class."""
import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class Test_City_Class(unittest.TestCase):
    """
    Check instance, type and class
    """

    def test_instance(self):
        """
        Check instance
        """
        my_city = City()
        self.assertIsInstance(my_city, City)
        self.assertIsInstance(my_city, BaseModel)
        my_city2 = City()
        self.assertTrue(type(my_city), type(my_city2))


class Test_City_Attributes(unittest.TestCase):
    """
    This class contains all tests of assignation of attributes.
    Public class attributes:
        state_id (str)
        name (str)
    """
    def test_correct_attributes(self):
        """Test assignation of state id and name."""
        new_city = City()
        new_state = State()
        new_city.state_id = new_state.id
        new_city.name = "Ba Sing Se"
        self.assertEqual(new_city.state_id, new_state.id)
        self.assertIsInstance(new_city.id, str)
        self.assertIsInstance(new_city.name, str)
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)


class TestCityMethods(unittest.TestCase):
    """
    Test all inherited methods.
    """
    def test_to_dict(self):
        """
        Check dict method"""
        new_city = City()
        new_city.name = "Ba Sing Se"
        new_city.save()
        new_city_json = new_city.to_dict()
        self.assertIsInstance(new_city_json, dict)

    def test_str(self):
        """
        Check str method
        """
        new_city = City()
        string = "[City] ({}) {}".format(new_city.id, new_city.__dict__)
        self.assertIsInstance(new_city.__str__(), str)
        self.assertEqual(new_city.__str__(), string)

    def test_creation_with_dict(self):
        """
        Check creation of instance with dictionary.
        """
        new_city = City()
        new_city.name = "Mordor"
        new_state = State()
        new_city.state_id = new_state.id
        another_city = City(new_city.to_dict())
        self.assertEqual(new_city.name, another_city.name)
        self.assertEqual(new_city.state_id, another_city.state_id)
