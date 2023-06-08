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
        self.room = Room.find_room_by_id(1)
        self.defeated = []
        self.character = inventory.character
        self.inventory = inventory

    def attack(self, attack):
        enemy = self.room.enemy
        inventory_names = (item.item_name for item in self.inventory.items)
        if attack in inventory_names and attack == enemy.fight_mechanics[0]:
            enemy.fight_mechanics.pop(0)
            print("attack success language")
            if not enemy.fight_mechanics:
                self.enemy_defeated()
        else:
            self.take_damage()
                
    def take_damage(self):
        self.character.health -= self.room.enemy.level
        sql = "UPDATE characters SET health=:1 WHERE id=:2"
        CURSOR.execute(sql, (self.character.health,self.character.id))
        print("attack failed language")    
            
    def enemy_defeated(self):
        print(f"You have defeated {self.room.enemy.enemy_name}")
        if self.room.item: 
            self.inventory.add_new_item(self.room.item)
            self.defeated.append(self.room.enemy)
    
    def game_over(self): 
        print("game over language")
        print("would you like to play again?")
    
    def update_room(self, id):
        self.room = Room.find_room_by_id(id)

    def is_enemy_defeated(self):
        return self.room.enemy in self.defeated if self.room.enemy else True
