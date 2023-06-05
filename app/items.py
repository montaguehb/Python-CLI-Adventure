import sqlite3

CONNECTER = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTER.cursor()

class Item():
    all = []
    def __init__(self, id, item_name, item_description, item_type):
        self.id = id
        self.item_name = item_name
        self.item_description = item_description
        self.item_type = item_type
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if not hasattr(self, "id"):
            self._id = id
        else:
            raise AttributeError
        
    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, item_name):
        if isinstance(item_name, str):
            self._item_name = item_name
        else:
            raise AttributeError
        
    @property
    def item_description(self):
        return self._item_name
    
    @item_description.setter
    def item_description(self, item_description):
        if isinstance(item_description, str):
            self._item_description = item_description
        else:
            raise AttributeError
        
    @property
    def item_type(self):
        return self._item_type
    
    @item_type.setter
    def item_type(self, item_type):
        if isinstance(item_type, str):
            self._item_type = item_type
        else:
            raise AttributeError
    
items = CURSOR.execute("SELECT * FROM items").fetchall()
for item in items:
    Item(item.items())