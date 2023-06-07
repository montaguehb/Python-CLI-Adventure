import sqlite3
from app.rooms import Room
from app.character import Character


CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()

class Floor():
    def __init__(self, room, character):
        self.room = room
        self.character = character
        
