import sqlite3
from scripts.items import Item
from scripts.enemies import Enemy 

CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()

class Room():
    """_summary_
    class method to find room by id
    method to generate new room instance from sql query
    """
    def __init__(self, id, item, enemy, north, south, west, east):
        self.id = id
        self.item = Item.find_item_by_id(item)
        self.enemy = Enemy.find_enemy_by_id(enemy)
        self.directions = {"north": north,
                           "south": south,
                           "west": west,
                           "east": east}
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
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        if isinstance(item, Item) or item is None:
            self._item = item
        else:
            raise AttributeError("item is immutable and must be of type item")
        
    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, enemy):
        if isinstance(enemy, Enemy) or enemy is None:
            self._enemy = enemy
        else:
            raise AttributeError("enemy is immutable and must be of type enemy")        

    @property
    def directions(self):
        return self._directions

    @directions.setter
    def directions(self, directions):
        self._directions = {}
        for key, value in directions.items():
            if isinstance(value, int) and value >= 0:
                self._directions[key] = value
            else:
                raise AttributeError("This needs to be a valid direction: north, south, west or east")

    @classmethod
    def find_room_by_id(cls, id):
        sql="SELECT * FROM rooms WHERE id=?"
        try:
            if isinstance(id, int):
                return cls.new_room(CURSOR.execute(sql, (id, )).fetchone())
            else:
                raise AttributeError("id is immutable and must be of type int")
        except Exception as e:
            print(e)
    
    def room_text(self):
        return "room text"
            
    @classmethod
    def new_room(cls, rooms):
        return Room(*rooms)

