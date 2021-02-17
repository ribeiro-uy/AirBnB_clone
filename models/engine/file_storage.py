#!/usr/bin/python3
"""
This module contains the methods for serialization/deserialization
and also save the data in files.
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage():
    """this class serializes json to a file and
    deserializes from a file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """set the __objects with obj in the key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to a JSON path from __file_path
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserialize the JSON file to __objects (only if JSON file exists).
        """
        if path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as f:
                    objdict = json.load(f)
                    for o in objdict.values():  # Traverse only through values
                        cls_name = o["__class__"]
                        del o["__class__"]  # Remove class name from dictionary
                        self.new(eval(cls_name)(**o))  # Create new instance
            except Exception:
                pass
