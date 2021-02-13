#!/usr/bin/env python3
""" This module contains the class BaseModel."""
from uuid import uuid4
from datetime import datetime
# uuid4 is a method that creates a random id.
# datetime is a class that contains several methods to interact with its data.


class BaseModel():
    """This class is the base class for other classes."""
    def __init__(self, *args, **kwargs):
        """Initialize an instance of this class."""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key in kwargs:
            if key is not "__class__" and hasattr(self, key):
                if key is "updated_at" or key is "created_at":
                    kwargs[key] = datetime.strptime(kwargs[key],
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns the string representation of an instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary with all key/values of the instance."""
        ret = dict(self.__dict__)
        ret["__class__"] = self.__class__.__name__
        ret["created_at"] = datetime.isoformat(self.created_at)
        ret["updated_at"] = datetime.isoformat(self.updated_at)

        return ret
