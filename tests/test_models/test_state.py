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

    def test_incorrect_assignation(self):
        """Test name with values other than a string."""
        pass
