#!/usr/bin/python3
# the file storage class
# serialization & deserialization of obj instances
# class that serializes instances to a JSON file &
# deserializes JSON file back to instances

import datetime
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


"""FileStorage class module."""


class FileStorage():

    __file_path = "file.json"
    __objects = {}

    # public instance methods

    def all(self):
        __objects = self.__dict__
        return __objects

    def new(self, obj):
        # the __objects key is created & assigned to obj_key
        # combine the classname with the objects id
        obj_key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[obj_key] = obj

    # serialize the object instance as a file
    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)
    
    # method to deserialize json file to obj
    def reload(self):
        # check if file is created 
        if not os.path.isfile(FileStorage.__file_path):
            return
        # write encoded file into the attribute
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {m: self.save()[n["__class__"]](**n)
                        for m, n in obj_dict.items()}
            FileStorage.__objects = obj_dict

