#!/usr/bin/python3
"""
This module contains the methods for serialization/deserialization
and also save the data in files.
"""
import json
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
        try:
            with open(FileStorage.__file_path, 'r') as f:
                # all_dicts = json.load(f)
                # for i in all_dicts.values():
                    # print(i)
                # print("this is where all objs should be: {}".format(FileStorage.__objects))
                # for key, value in all_dicts.items():
                    # Loop through dictionary of dictionaries,
                    # creating an instance of the class for each dictionary.
                    # cls_name is the class for the current object dict.
                #    cls_name = value.get('__class__')
                #    del value["__class__"]
                    # eval tries to execute the string within it.
                #    inst = eval(cls_name + '(**value)')

                    # Save new instance in __objects.
                #    self.new(inst)
                objdict = json.load(f)
                for o in objdict.values():  # Traverse only through values
                    cls_name = o["__class__"]
                    del o["__class__"]  # Remove class name from dictionary
                    self.new(eval(cls_name)(**o))  # Create new instance
        except FileNotFoundError:
            pass

