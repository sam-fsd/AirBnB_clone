#!/usr/bin/python3
"""Defines a FileStorage class"""

import json

class FileStorage:
    """ serializes instances to a JSON file
        and deserializes JSON file to instances

        Attributes:
            __file_path (str): File path to the JSON file
            __objects (dict): Stores all objects
    """
    __file_path = '/root/AirBnB_clone/data_file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        obj_id = obj.id
        obj_classname = type(obj).__name__
        obj_key = f"{obj_classname}.{obj_id}"
        self.__objects[obj_key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if len(self.__file_path) != 0:
            try:
                with open(self.__file_path, encoding='utf-8') as f:
                    self.__objects = json.load(f)
            except:
                pass
