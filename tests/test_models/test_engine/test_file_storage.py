import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from file_storage import FileStorage

class TestFileStorage_instantiation(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_add_new_object(self):
        user = User()
        self.storage.add_new_object(user)
        objects = self.storage.get_all_objects()
        self.assertIn("User." + user.id, objects)

    def test_save_object_to_file(self):
        user = User()
        self.storage.add_new_object(user)
        self.storage.save_object_to_file()
        self.assertTrue(os.path.exists("file.json"))

    def test_load_objects_from_file(self):
        user = User()
        self.storage.add_new_object(user)
        self.storage.save_object_to_file()
        new_storage = FileStorage()
        new_storage.load_objects_from_file()
        objects = new_storage.get_all_objects()
        self.assertIn("User." + user.id, objects)


if __name__ == "__main__":
    unittest.main()
