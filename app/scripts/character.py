import sqlite3
import sys
CONNECTER = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTER.cursor()

class Character():
    def __init__(self, id=0, username="", highest_score=0, health=10, inventory=None):
        self.id = id
        self.username = username.lower()
        self.health = health
        self.highest_score = highest_score
        self.score = 0
        
    @property
    def current_room(self):
        return self._current_room
    
    @current_room.setter
    def current_room(self, current_room):
        if isinstance(current_room, int):
            self._current_room = current_room
        else:
            raise AttributeError("current_room must be of type int")
    
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
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if(username == "bobby"):
            sql = "DELETE FROM characters"
            CURSOR.execute(sql)
            CONNECTER.commit()
            print("You have been banned from the game", style="failure")
            sys.exit()   
        elif isinstance(username, str):
            self._username = username
        else:
            raise AttributeError("username must be of type str")
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, health):
        if isinstance(health, int):
            self._health = health
        else:
            raise AttributeError("health must be of type int")
        
    @property
    def highest_score(self):
        return self._highest_score
    
    @highest_score.setter
    def highest_score(self, highest_score):
        if isinstance(highest_score, int):
            self._highest_score = highest_score
        else:
            raise AttributeError("highest_score must be of type int")
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int):
            self._score = score
        else:
            raise AttributeError("score must be of type int")
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM characters WHERE id = ?"
        return cls.new_from_db(*CURSOR.execute(sql, (id,)).fetchone())
    
    @classmethod
    def find_by_username(cls, username):
        sql = "SELECT * FROM characters WHERE username=?"
        try:
            return cls.new_from_db(*CURSOR.execute(sql, (username,)).fetchone())
        except TypeError:
            return None
    
    @classmethod
    def new_from_db(cls, *args):
        return cls(*args) if args[0] else None
    
    def add_to_db(self):
        if Character.find_by_username(self.username):
            self.update_id_from_db()
            Warning("Character already exists in database")
        sql = "INSERT INTO characters (username, health, highest_score) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (self.username, self.health, self.highest_score))
        CONNECTER.commit()
        self.update_id_from_db()
            
    def update_id_from_db(self):
        try:
            self._id = CURSOR.execute("SELECT id FROM characters WHERE id=?", (self.id, )).fetchone()[0]
        except Exception as e:
            print(e)