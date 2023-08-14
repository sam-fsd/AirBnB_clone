#1/usr/bin/python3
"""Defines a City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City model inheriting from BaseModel

        Attributes:
            state_id (str): The State id
            name (str): City name
    """
    state_id = ''
    name = ''
