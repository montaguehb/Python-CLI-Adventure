import sqlite3
from scripts.rooms import Room
from scripts.items import Item
from scripts.enemies import Enemy

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
    def __init__(self):
        self.rooms = self.get_all_rooms()
        self.current_room = self.rooms[0]
        self.defeated = []
        
    def get_all_rooms(self):
        sql = "SELECT * FROM rooms"
        return [Room(room[0],
                     Item.find_item_by_id(1), 
                     Enemy.find_enemy_by_id(1),
                     room[3],
                     room[4],
                     room[5],
                     room[6]) 
                for room in CURSOR.execute(sql).fetchall()]
        