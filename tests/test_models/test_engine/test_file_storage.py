#!/usr/bin/python3
""" This module contains all tests for the file_storage module."""
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from os import path


class TestFileStorage(unittest.TestCase):
    """ Class for the creation of tests for the file_storage module

    """

    # Test creation of new objects
    def test_objects(self):
        """ Test....

        """
        inst1 = BaseModel()
        inst1.save()

        # Check if file is created
        self.assertTrue(path.exists('file.json'))

        # Check if file is not empyty
        self.assertTrue(path.getsize('file.json') > 0)

        # Test the all() method through the storage in INIT
        objects = storage.all()  # In this case this shouldn't be empty
        self.assertTrue(len(objects) > 0)

        # Test to check if is instance of the class
        self.assertIsInstance(inst1, BaseModel)

        # Test to check if instance is correctly stored in __objects
        inst2 = BaseModel()
        storage.new(inst2)  # New() saves the object in __objects
        all_objs = storage.all()  # All() returns __objects
        list_objs = list(all_objs.values())
        self.assertIn(inst2, list_objs)

        # Test reload() method
        storage.reload()  # Load the dickts in file.json
        new_all_objs = storage.all()  # Get the return of the __objects
        # All_objs == new_all_objs? Answers below
        self.assertEqual(len(all_objs), len(new_all_objs))
        # Yes, indeed. Yeppity!


if __name__ == '__main__':
    unittest.main()
