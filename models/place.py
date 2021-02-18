#!/usr/bin/python3
"""This module contains the class Place.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Attributes:
        city_id (str): the City.id
        user_id (str): the User.id
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): default: 0
        number_bathrooms (int): default: 0
        max_guest (int): default: 0
        price_by_night (int): default: 0
        latitude (float): default: 0.0
        longitude(float): default: 0.0
        amenity_ids: the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
