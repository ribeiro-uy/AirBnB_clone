#!/usr/bin/env python3
"""This module contains all unittests for the BaseModel class."""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import models
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    """class for creation of tests for base_model module
    """

    def test_instance_type_class(self):
        """
        Checks for a instance of the class
        """
        instance1 = BaseModel()
        self.assertIsInstance(instance1, BaseModel)
        instance2 = BaseModel()
        self.assertIsInstance(instance2, BaseModel)
        self.assertTrue(type(instance1) == type(instance2))

    def test_str_method(self):
        """
        Checks str method
        """
        instance3 = BaseModel()
        string = "[{}] ({}) {}".format(instance3.__class__.__name__,
                                       instance3.id, instance3.__dict__)

        self.assertEqual(str(instance3), string)

    def test_attributes(self):
        """ Test the attributes in different cases
        """
        inst_1 = BaseModel()
        # test if id is string
        self.assertIsInstance(inst_1.id, str)
        inst_2 = BaseModel()
        # test different id
        self.assertNotEqual(inst_1.id, inst_2.id)
        # test if created_at is datetime
        self.assertIsInstance(inst_1.created_at, datetime)
        # test if update_at is datetime
        self.assertIsInstance(inst_1.updated_at, datetime)

    def test_save(self):
        """ Testing the save method
        """
        inst_1 = BaseModel()
        # test the updated_at before and after save()
        first_updated_at = inst_1.updated_at
        inst_1.save()
        second_updated_at = inst_1.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)
        # test the type of updated_at after save()
        self.assertIsInstance(inst_1.updated_at, datetime)

    def test_to_dict(self):
        """ Test to_dict method.
        """
        inst_1 = BaseModel()
        dict_1 = inst_1.to_dict()
        # Test type dict
        self.assertIsInstance(dict_1, dict)
        inst_1.save()
        # Test type
        dict_2 = inst_1.to_dict()
        # Test if dictionary updates automatically
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])

    def test_creation_with_dict(self):
        """Create instance by dictionary.
        """
        inst_10 = BaseModel()
        dict_10 = inst_10.to_dict()
        inst_20 = BaseModel(dict_10)
        self.assertIsInstance(inst_20, BaseModel)


class TestBaseModelInteractions(unittest.TestCase):
    """This class contains all tests regarding the interactions
    of BaseModel with other classes."""

    def test_imported_classes(self):
        """Test storage."""
        inst1 = BaseModel()
        old_dict = models.storage.all()
        self.assertIsInstance(old_dict, dict)
        self.assertIsInstance(models.storage, FileStorage)
        inst1.save()
        models.storage.new(inst1)
        new_dict = models.storage.all()
        self.assertEqual(old_dict, new_dict)
        assert os.path.exists("file.json") == 1
