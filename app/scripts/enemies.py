import sqlite3

CONNECTOR = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTOR.cursor()

class Enemy():
    def __init__(self,id,enemy_name,level,type,fight_mechanics):
        self.id = id
        self.enemy_name = enemy_name
        self.level = level
        self.type = type
        self.fight_mechanics = fight_mechanics
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if not hasattr(self, "id") and isinstance(id, int):
            self._id = id
        else:
            raise AttributeError("id is immutable and must be of type int")
        
    @property
    def enemy_name(self):
        return self._enemy_name
    
    @enemy_name.setter
    def enemy_name(self, enemy_name):
        if isinstance(enemy_name, str):
            self._enemy_name = enemy_name
        else:
            raise AttributeError("enemy_name must be of type str")

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self,level):
        if isinstance(level,int) and 1<= level <=10:
            self._level = level
        else:
            raise AttributeError("level must be of type int and between 1-10 inclusive")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if type in ("easy", "medium" , "hard"):
            self._type = type
        else:
            raise AttributeError("type must be 'easy', 'medium', or 'hard'")
        
    @property
    def fight_mechanics(self):
        return self._fight_mechanics
    
    @fight_mechanics.setter
    def fight_mechanics(self, fight_mechanics):
        if isinstance(fight_mechanics,str):
            self._fight_mechanics = fight_mechanics.split(", ")
        else:
            raise AttributeError("fight_mechanics must be of type str")
        
    @classmethod
    def find_enemy_by_id(cls,id):
        sql="SELECT * FROM enemies WHERE id=?"
        try:
            if isinstance(id,int):
                return cls.new_from_db(CURSOR.execute(sql, (id, )).fetchone())
            elif id == "Null":
                return None
            else:
                raise ValueError
        except Exception:
            return None
            
    @classmethod
    def new_from_db(cls,enemy):
        return Enemy(*enemy)