import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_generation(self):
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        obj_dict = self.model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.model.id)
        self.assertEqual(obj_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str(self):
        obj_str = str(self.model)
        self.assertIsInstance(obj_str, str)
        self.assertIn('BaseModel', obj_str)
        self.assertIn(self.model.id, obj_str)
        self.assertIn(self.model.created_at.strftime('%Y-%m-%dT%H:%M:%S'), obj_str)

if __name__ == '__main__':
    unittest.main()
