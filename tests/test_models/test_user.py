#!/usr/bin/python3
"""This module contains all unittests for the User class."""
import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
import models


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


class TestUserStorage(unittest.TestCase):
    """Test the correct storage of User.
    Storage methods:
        all()
        new(obj)
        save()
        reload()
    """
    def test_storage_class(self):
        """Test the imported variable storage."""
        self.assertIsInstance(models.storage, FileStorage)

    def test_storage_new(self):
        """Test if storage saves a User in the dictionary."""
        neo = User()
        neo.email = "neo@matrix.net"
        neo.password = "SinClave"
        neo.first_name = "Thomas"
        neo.last_name = "Anderson"
        neo.save()
        models.storage.new(neo)
        all_objs = models.storage.all()
        self.assertNotIn(neo, all_objs)

    def test_save_reload(self):
        """Test if storage correctly serializes and deserializes."""
        neo = User()
        neo.email = "neo@matrix.net"
        neo.password = "SinClave"
        neo.first_name = "Thomas"
        neo.last_name = "Anderson"
        neo.save()
        all_objs = models.storage.all()
        models.storage.new(neo)
        models.storage.reload()
        new_objs = models.storage.all()
        self.assertEqual(all_objs, new_objs)

