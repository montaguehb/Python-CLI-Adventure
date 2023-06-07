import sqlite3
from scripts.rooms import Room

CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()

class Floor():
    def __init__(self, room):
        self.room = room
