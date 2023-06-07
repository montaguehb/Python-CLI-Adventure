import sqlite3

CONNECTOR = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTOR.cursor()

class Item():
    """_summary_
    class method to find item by id
    class method to create new item instance from SQL query
    """
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
        if not hasattr(self, "_id") and isinstance(id, int):
            self._id = id
        else:
            raise AttributeError("id is immutable and must be of type int")
        
    @property
    def item_name(self):
        return self._item_name
    
    @item_name.setter
    def item_name(self, item_name):
        if isinstance(item_name, str):
            self._item_name = item_name
        else:
            raise AttributeError("item_name must be of type str")
        
    @property
    def item_description(self):
        return self._item_name
    
    @item_description.setter
    def item_description(self, item_description):
        if isinstance(item_description, str):
            self._item_description = item_description
        else:
            raise AttributeError("Item_description must be of type str")
    
        
    @property
    def item_type(self):
        return self._item_type
    
    @item_type.setter
    def item_type(self, item_type):
        if isinstance(item_type, str):
            self._item_type = item_type
        else:
            raise AttributeError("Item_type must be of type str")
    
    @classmethod
    def find_item_by_id(cls, id):
        sql="SELECT * FROM items WHERE id=?"
        try:
            if isinstance(id, int):
                return cls.new_from_db(CURSOR.execute(sql, (id, )).fetchone())
            else:
                raise ValueError
        except Exception as e:
            print(e)
    
    @classmethod
    def new_from_db(cls, args):
        return Item(*args)
    
# items = CURSOR.execute("SELECT * FROM items").fetchall()
# for item in items:
#     Item(item.items())