#!/usr/bin/python3
"""This module contains all tests for the State class."""
import unittest
from models.state import State
from models.base_model import BaseModel
class TestStateAttributes(unittest.TestCase):
    """Test assignation of attributes."""
    def test_correct_assignation(self):
        """Class State has attribute name, should be string."""
        new_state = State()
        new_state.name = "Not Minnessota"
        self.assertIsInstance(new_state, State)
        self.assertIsInstance(new_state, BaseModel)
        self.assertIsInstance(new_state.name, str)
class TestStateMethods(unittest.TestCase):
    """
    Test all inherited methods.
    """
    def test_to_dict(self):
        """
        Check dict method.
        """
        new_state = State()
        new_state.first_name = "no"
        new_state.last_name = "thats confidential"
        new_state.save()
        new_state_json = new_state.to_dict()
        self.assertIsInstance(new_state_json, dict)
    def test_str(self):
        """
        Check str method.
        """
        new_state = State()
        string = "[State] ({}) {}".format(new_state.id, new_state.__dict__)
        self.assertIsInstance(new_state.__str__(), str)
        self.assertEqual(new_state.__str__(), string)
    def test_creation_with_dict(self):
        """
        Check creation of instance with dictionary.
        """
        new_state = State()
        new_state.name = "Minnesotta"
        another_state = State(new_state.to_dict())
        self.assertEqual(new_state.name, another_state.name)
