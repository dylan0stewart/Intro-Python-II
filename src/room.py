from typing import List
from item import Item 

class Room:
    def __init__(self, name, description, items=[], **kwargs):
        self.name = name
        self.description = description
        self.items = items

    def remove_item(self, item):
        self.items.remove(item)

    def add_item(self, item):
        self.items.append(item) 