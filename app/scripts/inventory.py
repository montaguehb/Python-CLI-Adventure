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
        self.character = character
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
    def character(self):
        return self._character
    
    @character.setter
    def character(self, character):
        if isinstance(character, Character):
            self._character = character
        else:
            raise AttributeError
    
    def add_new_item(self, item):
        if isinstance(item, Item):
            self.items.append(item)
            self.update_new_inventory_db(item)
            print(f"You recieved the {item.item_name} command. This is used to {item.item_description}")
        else:
            raise AttributeError("item must be of type Item")
        
    def update_new_inventory_db(self, item):
        sql= "INSERT INTO inventory (character_id, item_id) VALUES(?, ?)"
        CURSOR.execute(sql, (self.character.id, item.id))
        CONNECTER.commit()


    def pull_existing_inventory(self):
        sql= "SELECT * from inventory"
        inventory = CURSOR.execute(sql).fetchone()
        self.items.append(Item.find_by_id(inventory[2]))

        