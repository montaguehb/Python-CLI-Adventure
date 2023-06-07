import sqlite3
from scripts.rooms import Room
from scripts.items import Item
from scripts.enemies import Enemy
from scripts.character import Character
from scripts.inventory import Inventory

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
    def __init__(self, character):
        self.rooms = self.get_all_rooms()
        self.current_room = self.rooms[0]
        self.defeated = []
        self.character = character
        
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

    def attack(self, input):
        enemy = self.current_room.enemy
        inventory= self.character.invetory
        inventory_names = (item.item_name for item in inventory)
        if input in inventory_names and input == enemy.fight_mechanics[0]:
            enemy.fight_mechanics.pop(0)
            print("attack success language")
            if enemy.fight_mechanics == []:
                self.enemy_defeat()
        else:
            self.take_damage()
                
    def take_damage(self):
        self.character.health -= self.enemy.level
        sql = "UPDATE characters SET health=:1, WHERE id=:2"
        CURSOR.execute(sql, (self.character.health,self.character.id))
        print("attack failed language")
        if self.character.health <= 0:
            self.game_over()        
            
    def enemy_defeat(self):
        print(f"You have defeated {self.enemy.name}") 
        print(f"You recieved the {self.room.item.item_name} command. This is used to {self.room.item.item_description}")
        self.character.inventory.add_new_item(self.room.item)
        #confirm above is the correct Inventory function
        #Navigation script
    
    def game_over(self): 
        print("game over language")
        print("would you like to play again?")
        if input == "play_again":
            self.play_again()
