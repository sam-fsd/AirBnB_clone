#!/usr/bin/python3
"""Defines a Place class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ A model for a place

        Attributes:
            city_id (str): The city id
            user_id (str): The User id
            name (str): Name of the place
            description (str): Info about the place
            number_rooms (int): Number of rooms
            number_bathrooms (int): Number of bathrooms
            max_guest (in): Maximum number of guests
            price_by_night (int): Price for a night
            latitude (float): Latitude
            longitude (float): Longitude
            amenity_ids (list): List of amenity Ids
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
