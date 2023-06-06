import sqlite3
from app.scripts.character import Character
from app.scripts.items import Item
CONNECTER = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTER.cursor()

class Inventory():
    def __init__(self, id=0, character=None, item=None):
        self.character_id = character.id
        self.items = []
        self.add_new_item(item)
    
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