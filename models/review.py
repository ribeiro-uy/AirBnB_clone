#!/usr/bin/python3
"""
This module contains the class Review, which inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    All methods are inherited from BaseModel.
    Attributes:
        place_id (str): the Place.id
        user_id (str): the User.id
        text (str): the text of the review
    """
    place_id = ""
    user_id = ""
    text = ""
