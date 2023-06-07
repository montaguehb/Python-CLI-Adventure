import sqlite3
from scripts.rooms import Room

CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()

class Floor():
    """_summary_
    method to update current room
    class method to generate rooms from db
    method to check each turn of battle
    update enemy of room to be defeated
    method to check if enemy has been defeated
    """
    def __init__(self, rooms):
        self.rooms = self.get_all_rooms()

    def get_all_rooms(self):
        sql = "SELECT * FROM floors"
        return [Room(room[1], room[2]) for room in CURSOR.execute(sql).fetchall()]