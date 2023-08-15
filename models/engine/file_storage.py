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
    __file_path = 'data_file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with
            key <obj class name>.id
        """
        obj_id = obj.id
        obj_classname = type(obj).__name__
        obj_key = f"{obj_classname}.{obj_id}"
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if len(FileStorage.__file_path) != 0:
            try:
                with open(FileStorage.__file_path, encoding='utf-8') as f:
                    FileStorage.__objects = json.load(f)
            except:
                pass
