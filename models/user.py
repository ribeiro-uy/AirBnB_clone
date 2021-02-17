#!/usr/bin/python3
"""
This module contains the class User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User inherits all methods from BaseModel.
    Attributes:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
