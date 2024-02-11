#!/usr/bin/python3
"""Implementation of a cutsom storage engine"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ A cutsom storage engine for storing objects in JSON format."""

    __file_path = "file.json"
    __objects = {}

    def get_all_objects(self):
        """Retrives all objects stored in the storage engine."""
        return FileStorage.__objects

    def add_new_object(self, obj):
        """Add a new object to the storage engine"""
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save_object_to_file(self):
        """Serialize __objects to the JSON file."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as fil:
            json.dump(objdict, fil)

    def load_objects_from_file(self):
        """Deserialize the JSON file."""
        try:
            with open(FileStorage.__file_path) as fil:
                objd = json.load(f)
                for o in objd.values():
                    class_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
