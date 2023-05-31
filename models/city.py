#!/usr/bin/python3
""" City Module for hbnb project """
from models.base_model import BaseModel


class City(BaseModel):
    """ the city class, contains state ID and name """
    state_id = ""
    name = ""
