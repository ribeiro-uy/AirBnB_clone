#!/usr/bin/python3
"""This module contains all unittests for the User class."""
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class Test_User_Class(unittest.TestCase):
    """
    Check instance, type and class
    """
    def test_instance(self):
        """
        Check instance
        """
        Neo = User()
        self.assertIsInstance(Neo, User)
        self.assertIsInstance(Neo, BaseModel)
        Trinity = User()
        self.assertTrue(type(Neo), type(Trinity))


class Test_User_Attributes(unittest.TestCase):
    """
    This class contains all tests of assignation of attributes.
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    def test_correct_attributes(self):
        """Test assignation of attributtes id and name."""
        Neo = User()
        Neo.email = "neo@matrix.net"
        Neo.password = "SinClave"
        Neo.first_name = "Thomas"
        Neo.last_name = "Anderson"
        self.assertIsInstance(Neo.email, str)
        self.assertIsInstance(Neo.password, str)
        self.assertIsInstance(Neo.first_name, str)
        self.assertIsInstance(Neo.last_name, str)
        self.assertIsInstance(Neo.created_at, datetime)
        self.assertIsInstance(Neo.updated_at, datetime)


class TestUserMethods(unittest.TestCase):
    """
    Test all inherited methods.
    """
    def test_to_dict(self):
        """
        Check dict method.
        """
        new_user = User()
        new_user.first_name = "no"
        new_user.last_name = "thats confidential"
        new_user.save()
        new_user_json = new_user.to_dict()
        self.assertIsInstance(new_user_json, dict)

    def test_str(self):
        """
        Check str method.
        """
        new_user = User()
        string = "[User] ({}) {}".format(new_user.id, new_user.__dict__)
        self.assertIsInstance(new_user.__str__(), str)
        self.assertEqual(new_user.__str__(), string)

    def test_creation_with_dict(self):
        """
        Check creation of instance with dictionary.
        """
        new_user = User()
        new_user.first_name = "Spike"
        new_user.last_name = "(Not a dog)"
        new_user.email = "notadog@ymail.com"
        new_user.password = "********"
        another_user = User(new_user.to_dict())
        self.assertEqual(new_user.first_name, another_user.first_name)
        self.assertEqual(new_user.last_name, another_user.last_name)
        self.assertEqual(new_user.email, another_user.email)
        self.assertEqual(new_user.password, another_user.password)

    def test_save(self):
        """
        Check save method.
        """
        new_user = User()
        new_user.first_name = "Oriental"
        new_user.last_name = "Spice"
        new_user_dict = new_user.to_dict()
        first_update = new_user_dict[updated_at]
        new_user.save()
        second_update = new_user_dict[updated_at]
        self.assertNotEqual(first_update, second_update)


class TestUserAttributes(unittest.TestCase):
    """Test the correct assignation of attribute values."""
    pass
