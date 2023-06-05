import sqlite3
from app.items import Item
from app.enemies import Enemy 

CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()

class Room():
    def __init__(self, id, item, enemy, top, bottom, left, right):
        self.id = id
        self.item = item
        self.enemy = enemy
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

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
def top(self):
    return self._top

@top.setter
def top(self, top):
    if isinstance(top, Room) or not top:
        self._top = top
    else:
        raise AttributeError("This needs to be a boolean")
    
@property
def bottom(self):
    return self._bottom

@bottom.setter
def bottom(self, bottom):
    if isinstance(bottom, Room) or not bottom:
        self._bottom = bottom
    else:
        raise AttributeError("This needs to be a boolean")
    
@property
def left(self):
    return self._left

@top.setter
def top(self, left):
    if isinstance(left, Room) or not left:
        self._left = left
    else:
        raise AttributeError("This needs to be a boolean")
    
@property
def right(self):
    return self._right

@right.setter
def right(self, right):
    if isinstance(right, Room) or not right:
        self._right = right
    else:
        raise AttributeError("This needs to be a boolean")



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
def new_room(cls, *rooms):
    return Room(*rooms)



