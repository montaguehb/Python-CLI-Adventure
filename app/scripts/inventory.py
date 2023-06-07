import sqlite3
from scripts.character import Character
from scripts.items import Item
CONNECTER = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTER.cursor()

class Inventory():
    """_summary_
    method to add new items to character inventory
    method to update db to match self.items
    """
    def __init__(self, character=None):
        self.character_id = character.id
        self.items = []
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if not hasattr(self, "_id") and isinstance(id, int):
            self._id = id
        else:
            raise AttributeError("id is immutable and must be of type int")
    
    @property
    def character_id(self):
        return self._character_id
    
    @character_id.setter
    def character_id(self, character_id):
        if isinstance(character_id, Character):
            self._character_id = character_id
        else:
            raise AttributeError
    
    def add_new_item(self, item):
        if isinstance(item, Item):
            self.items.append(item)
        else:
            raise AttributeError("item must be of type Item")