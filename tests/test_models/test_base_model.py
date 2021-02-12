#!/usr/bin/env python3
"""This module contains all unittests for the BaseModel class."""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_id_string(self):
        to_test = BaseModel()
        self.assertIsInstance(to_test.id, str)

    def test_more_parameters(self):
        to_test = BaseModel()


    def test_created_at(self):
        to_test = BaseModel()
        self.assertEqual(type)
    def test_noformat_in_created_at(self):
        to_test = BaseModel()
    def test_update_at(self):
        to_test = BaseModel()
    def test_noformat_updated_at(self):
        to_test = BaseModel()

    def test_str(self):

    def test_save(self):

    def test_to_dict(self):

    
    