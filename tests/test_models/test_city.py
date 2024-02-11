import unittest
from models.city import City

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.city = City()
        
    def test_attributes_initialization(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
        
    def test_attributes_assignment(self):
        self.city.state_id = "state123"
        self.city.name = "New York"
        
        self.assertEqual(self.city.state_id, "state123")
        self.assertEqual(self.city.name, "New York")

if __name__ == '__main__':
    unittest.main()
