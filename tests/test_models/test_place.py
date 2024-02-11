import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    
    def setUp(self):
        self.place = Place()
        
    def test_attributes_initialization(self):
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        
    def test_attributes_assignment(self):
        self.place.city_id = "city123"
        self.place.user_id = "user123"
        self.place.name = "Cozy House"
        self.place.description = "A beautiful house in the countryside"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 6
        self.place.price_by_night = 100
        self.place.latitude = 42.1234
        self.place.longitude = -71.5678
        self.place.amenity_ids = ["amenity1", "amenity2"]
        
        self.assertEqual(self.place.city_id, "city123")
        self.assertEqual(self.place.user_id, "user123")
        self.assertEqual(self.place.name, "Cozy House")
        self.assertEqual(self.place.description, "A beautiful house in the countryside")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 42.1234)
        self.assertEqual(self.place.longitude, -71.5678)
        self.assertEqual(self.place.amenity_ids, ["amenity1", "amenity2"])

if __name__ == '__main__':
    unittest.main()
