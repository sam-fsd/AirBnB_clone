#!/usr/bin/python3
""" Defines an Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ A model for amenity
        
        Attributes:
            name (str): Name of the amenity
    """
    name = ''
