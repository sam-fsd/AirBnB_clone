#!/usr/bin/python3
"""Defines a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review model class

        Attributes:
            place_id (str): The place id
            user_id (str): The user id
            text (str): The feedback
    """
    place_id = ''
    user_id = ''
    text = ''
