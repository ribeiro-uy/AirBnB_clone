#!/usr/bin/env python3
"""This module contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances."""
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__ + '.' + obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)."""
        all_dicts = []
        try:
            with open(FileStorage.__file_path, 'r') as file_open:
                for line in file_open:
                    all_dicts.append(json.loads(line))
            for value in all_dicts:
                # Loop through dictionary of dictionaries,
                # Creating an instance of the class for each dictionary.
                inst = eval(value)
                # Save new instance in __objects.
                # THIS IS NOT WORKING BUT WHY
                key = str(inst.__class__.__name__ + '.' + inst.id)
                FileStorage.__objects[key] = inst
        except:
            pass
