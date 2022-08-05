#!/usr/bin/python3
"""Module for thr place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class for representing place"""
    def __init__(self):
        self.city_id = ''
        self.user_id = ''
        self.name = ''
        self.description = ''
        self.number_rooms = 0
        self.nuber_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []


