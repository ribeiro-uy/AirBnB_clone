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
        self.assertIsInstance(objects, dict)

        # Test to check if is instance of the class
        self.assertIsInstance(inst1, BaseModel)

        # Test storage as instance of FileStorage
        self.assertIsInstance(storage, FileStorage)

        # Test new() method
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

    def test_file_storage(self):
        """Test creation of storage."""
        storage_test = FileStorage()
        self.assertIsInstance(storage_test, FileStorage)
        # Check that they are different instances.
        self.assertNotEqual(storage_test, storage)
        # Check reload method.
        storage_test.reload()
        all_objs = storage_test.all()
        # Check new method.
        len_first = len(all_objs)
        inst1 = BaseModel()
        storage_test.new(inst1)
        len_now = len(all_objs)
        self.assertNotEqual(len_first, len_now)
        storage_test.save()
        storage.save()
        new_objs = storage.all()
        # Check if both instances point to the same class variable
        self.assertEqual(all_objs, new_objs)


if __name__ == '__main__':
    unittest.main()
