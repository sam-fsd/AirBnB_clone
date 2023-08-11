#!/usr/bin/python3
"""Defines BaseModel class"""

from datetime import datetime
import uuid


class BaseModel:
    """Base/parent class"""
    def __init__(self):
        """Constructor method"""
        uuid_obj = uuid.uuid4()
        self.id = str(uuid_obj)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints the cls arributes"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        a_dict = self.__dict__

        a_dict[__class__] = "BaseModel"
        a_dict['created_at'] = a_dict['created_at'].isoformat()
        a_dict['updated_at'] = a_dict['updated_at'].isoformat()

        return a_dict
