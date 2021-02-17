#!/usr/bin/python3
"""This module contains all tests for the Place class,
as well as all methods it inherits.
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.user import User


class TestPlaceAttributes(unittest.TestCase):
    """Place attributes (public class attributes):

    city_id (str): the City.id
    user_id (str): the User.id
    name (str): name of the place
    description (str): description of the place
    number_rooms (int): default: 0
    number_bathrooms (int): default: 0
    max_guest (int): default: 0
    price_by_night (int): default: 0
    latitude (float): default: 0.0
    longitude(float): default: 0.0
    amenity_ids: the list of Amenity.id
    """

    def test_correct_assignation(self):
        """Test assignation of all attributes with correct values."""
        new_place = Place()
        new_place.user_id = "some_random_id_777"
        new_place.city_id = "some_city_id"
        new_place.name = "República Separatista Independiente de Bella Unión"
        new_place.description = "No extrañado"
        new_place.number_rooms = 4
        new_place.number_bathrooms = 4
        new_place.max_guest = 127
        new_place.price_by_night = 2
        new_place.latitude = 30.15
        new_place.longitude = 57.35
        # Test correct types.
        self.assertIsInstance(new_place, BaseModel)
        self.assertIsInstance(new_place.user_id, str)
        self.assertIsInstance(new_place.city_id, str)
        self.assertIsInstance(new_place.name, str)
        self.assertIsInstance(new_place.description, str)
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertIsInstance(new_place.number_bathrooms, int)
        self.assertIsInstance(new_place.max_guest, int)
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertIsInstance(new_place.latitude, float)
        self.assertIsInstance(new_place.longitude, float)

    def test_incorrect_assignation(self):
        """Test assignation of all attributes with correct values."""
        new_place = Place()
        new_place.user_id = 3.1416
        new_place.city_id = True
        new_place.name = None
        new_place.description = None
        new_place.number_rooms = "4"
        new_place.number_bathrooms = "yes"
        new_place.max_guest = 12.7
        new_place.price_by_night = 2.1
        new_place.latitude = 30
        new_place.longitude = 57
        # Test correct types.
        self.assertIsInstance(new_place, BaseModel)
        self.assertNotIsInstance(new_place.user_id, str)
        self.assertNotIsInstance(new_place.city_id, str)
        self.assertNotIsInstance(new_place.name, str)
        self.assertNotIsInstance(new_place.description, str)
        self.assertNotIsInstance(new_place.number_rooms, int)
        self.assertNotIsInstance(new_place.number_bathrooms, int)
        self.assertNotIsInstance(new_place.max_guest, int)
        self.assertNotIsInstance(new_place.price_by_night, int)
        self.assertNotIsInstance(new_place.latitude, float)
        self.assertNotIsInstance(new_place.longitude, float)

    def test_all_boolean_values(self):
        """Test boolean attributes."""
        new_place = Place()
        new_place.user_id = True
        new_place.city_id = True
        new_place.name = True
        new_place.description = False
        new_place.number_rooms = False
        new_place.number_bathrooms = False
        new_place.max_guest = True
        new_place.price_by_night = False
        new_place.latitude = True
        new_place.longitude = False
        self.assertNotIsInstance(new_place.user_id, str)
        self.assertNotIsInstance(new_place.city_id, str)
        self.assertNotIsInstance(new_place.name, str)
        self.assertNotIsInstance(new_place.description, str)
        self.assertIsInstance(new_place.number_rooms, int)
        self.assertIsInstance(new_place.number_bathrooms, int)
        self.assertIsInstance(new_place.max_guest, int)
        self.assertIsInstance(new_place.price_by_night, int)
        self.assertNotIsInstance(new_place.latitude, float)
        self.assertNotIsInstance(new_place.longitude, float)

    def test_all_none_values(self):
        """Test all attributes set as None."""
        new_place = Place()
        new_place.user_id = None
        new_place.city_id = None
        new_place.name = None
        new_place.description = None
        new_place.number_rooms = None
        new_place.number_bathrooms = None
        new_place.max_guest = None
        new_place.price_by_night = None
        new_place.latitude = None
        new_place.longitude = None
        self.assertNotIsInstance(new_place.user_id, str)
        self.assertNotIsInstance(new_place.city_id, str)
        self.assertNotIsInstance(new_place.name, str)
        self.assertNotIsInstance(new_place.description, str)
        self.assertNotIsInstance(new_place.number_rooms, int)
        self.assertNotIsInstance(new_place.number_bathrooms, int)
        self.assertNotIsInstance(new_place.max_guest, int)
        self.assertNotIsInstance(new_place.price_by_night, int)
        self.assertNotIsInstance(new_place.latitude, float)
        self.assertNotIsInstance(new_place.longitude, float)

    def test_creation_by_dictionary(self):
        """Test creation of instance with dictionary."""
        new_place = Place()
        new_place.user_id = "some_random_id_777"
        new_place.city_id = "some_city_id"
        new_place.name = "República Separatista Independiente de Bella Unión"
        new_place.description = "No extrañado"
        new_place.number_rooms = 4
        new_place.number_bathrooms = 4
        new_place.max_guest = 127
        new_place.price_by_night = 2
        new_place.latitude = 30.15
        new_place.longitude = 57.35
        new_place_dict = new_place.to_dict()
        test_creation = Place(new_place_dict)
        self.maxDiff = None
        self.assertEqual(test_creation.name, new_place.name)


class TestPlaceConnectionsWithOtherClasses(unittest.TestCase):
    """This class tests all assignation of attributes from other classes,
    such as: Place.user_id (assigned from class User), Place.city_id, etc.
    """
    def test_correct_assignation_with_instances(self):
        """Some values are the attributes of other instances."""
        new_place = Place()
        new_city = City()
        new_user = User()
        # Assign values to new_place
        new_place.user_id = "some_random_id_777"
        new_place.city_id = "some_city_id"
        new_place.name = "República Separatista Independiente de Bella Unión"
        new_place.description = "No extrañado"
        new_place.number_rooms = 4
        new_place.number_bathrooms = 4
        new_place.max_guest = 127
        new_place.price_by_night = 2
        new_place.latitude = 30.15
        new_place.longitude = 57.35
        # Assign values from other classes
        new_place.city_id = new_city.id
        new_place.user_id = new_user.id
        # Test type
        self.assertIsInstance(new_place.city_id, str)
        self.assertIsInstance(new_place.user_id, str)
        # Test correct assignation
        self.assertEqual(new_place.city_id, new_city.id)
        self.assertEqual(new_place.user_id, new_user.id)
