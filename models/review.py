#!/usr/bin/python3
"""creates the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """manages the reviews."""
    place_id = ""
    user_id = ""
    text = ""
