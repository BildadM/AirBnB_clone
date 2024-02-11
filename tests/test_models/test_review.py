import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_review_initialization(self):
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attributes_assignment(self):
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This is a great place!"
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "This is a great place!")


if __name__ == "__main__":
    unittest.main()
