#!/usr/bin/python3
""" Defines State class"""

import models.base_model import BaseModel


class State(BaseModel):
    """A child class of BaseModel

        Attributes:
            name (str): State name
    """
    name = ""
