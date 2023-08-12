#!/usr/bin/python3
"""Defines BaseModel class"""

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """Base/parent class"""
    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value,  "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            uuid_obj = uuid.uuid4()
            self.id = str(uuid_obj)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
            storage.new()

    def __str__(self):
        """Prints the cls arributes"""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        a_dict = self.__dict__

        a_dict['__class__'] = "BaseModel"
        a_dict['created_at'] = a_dict['created_at'].isoformat()
        a_dict['updated_at'] = a_dict['updated_at'].isoformat()

        return a_dict
