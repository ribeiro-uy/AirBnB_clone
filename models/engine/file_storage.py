#!/usr/bin/env python3
"""This module contains a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances."""
import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__ + '.' + obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w") as f:
            for key in self.__objects:
                json.dump(self.__objects[key], f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists; otherwise, do nothing. If the file
        doesn’t exist, no exception should be raised)."""
        try:
            with open(self.__file_path, r) as file_open:
                new_dict = json.load(file_open)
            
            for key in new_dict:
                self.__objects[key] = 
        except:
            pass 