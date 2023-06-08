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
        self.item = item
        self.enemy = enemy
        self.north = north
        self.south = south
        self.west = west
        self.east = east

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
    if isinstance(item, Item):
        self._item
    else:
        raise AttributeError("item is immutable and must be of type int")
    
@property
def enemy(self):
    return self._enemy

@enemy.setter
def enemy(self, enemy):
    if isinstance(enemy, Enemy):
        self._enemy
    else:
        raise AttributeError("enemy is immutable and must be of type int")
    

@property
def north(self):
    return self._north

@north.setter
def north(self, north):
    if isinstance(north, int) or north == 1:
        self._north = north
    else:
        raise AttributeError("This needs to be a valid direction: north, south, west or east")
    
@property
def south(self):
    return self._south

@south.setter
def south(self, south):
    if isinstance(south, int) or south == 1:
        self._south = south
    else:
        raise AttributeError("This needs to be a valid direction: north, south, west or east")
    
@property
def west(self):
    return self._west

@north.setter
def north(self, west):
    if isinstance(west, Room) or west == 1:
        self._west = west
    else:
        raise AttributeError("This needs to be a valid direction: north, south, west or east")
    
@property
def east(self):
    return self._east

@east.setter
def east(self, east):
    if isinstance(east, Room) or east ==1:
        self._east = east
    else:
        raise AttributeError("This needs to be a valid direction: north, south, west or east")



@classmethod
def find_room_by_id(cls, id):
    sql="SELECT * FROM rooms WHERE id=?"
    try:
        if isinstance(id, int):
            return cls.new_room(CURSOR.execute(sql, (id, )).fetchone())
        else:
            raise ValueError
    except Exception as e:
        print(e)

@classmethod
def new_room(cls, rooms):
    return Room(*rooms)



