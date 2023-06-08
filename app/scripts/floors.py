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
    def __init__(self, inventory):
        self.rooms = self.get_all_rooms()
        self.current_room = self.rooms[0]
        self.defeated = []
        self.character = inventory.character
        self.inventory = inventory
        
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

    def attack(self, attack):
        enemy = self.current_room.enemy
        inventory_names = (item.item_name for item in self.inventory)
        if attack in inventory_names and attack == enemy.fight_mechanics[0]:
            enemy.fight_mechanics.pop(0)
            print("attack success language")
            if enemy.fight_mechanics == []:
                self.enemy_defeated()
        else:
            self.take_damage()
                
    def take_damage(self):
        self.character.health -= self.enemy.level
        sql = "UPDATE characters SET health=:1, WHERE id=:2"
        CURSOR.execute(sql, (self.character.health,self.character.id))
        print("attack failed language")    
            
    def enemy_defeated(self):
        print(f"You have defeated {self.enemy.name}") 
        print(f"You recieved the {self.room.item.item_name} command. This is used to {self.room.item.item_description}")
        self.character.add_new_item(self.room.item)
        self.defeated.append(self.current_room.enemy)
    
    def game_over(self): 
        print("game over language")
        print("would you like to play again?")
    
    def update_current_room(self, id):
        self.current_room = Room.find_room_by_id(id)

    def is_enemy_defeated(self):
        return self.current_room.enemy in self.defeated