import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_amenity_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_amenity_name_assignment(self):
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")


if __name__ == "__main__":
    unittest.main()
