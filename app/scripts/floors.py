import sqlite3
import random
from scripts.rooms import Room
from scripts.items import Item
from scripts.enemies import Enemy
from scripts.character import Character
from scripts.inventory import Inventory

CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()

class Floor():
    def __init__(self, inventory):
        self.room = Room.find_room_by_id(1)
        self.defeated = []
        self.character = inventory.character
        self.inventory = inventory
        self.attack_success = []
        self.attack_fail = []
    
    @property
    def attack_success(self):
        return self._attack_success
    
    @attack_success.setter
    def attack_success(self, attack_success):
        with open("./app/txt/success.txt", "r") as f:
            self._attack_success = f.read().splitlines()
        # sql = "SELECT * FROM text WHERE used=?"
        # self._attack_success = [text[1] for text in CURSOR.execute(sql, ("success", )).fetchall()]
                        
    def enemy_encounter(self):
        print(f"oh look a bad guy")
        print(f"looks like they are weak agaist {self.enemy_weaknesses()}")
        if len(self.enemy_weaknesses())>1:
            print("the order is important")
        
    def enemy_weaknesses(self):
        sql= "SELECT item_description FROM items WHERE item_name=?"
        return([CURSOR.execute(sql, (mechanic,)).fetchone()[-1] for mechanic in self.room.enemy.fight_mechanics])
    
    def enemy_attack_response(self):
        print("the enemy name is getting closer. Attack again!")
        print(f"it's weak against {self.enemy_weaknesses()}")
    
    def attack(self, attack):
        enemy = self.room.enemy
        inventory_names = (item.item_name for item in self.inventory.items)
        if attack in inventory_names and attack == enemy.fight_mechanics[0]:
            enemy.fight_mechanics.pop(0)
            print(self.attack_success[random.randint(0, len(self.attack_success) - 1)].format(
                enemy_name = self.room.enemy.enemy_name,
                item_name=attack))
            if not enemy.fight_mechanics:
                self.enemy_defeated()
        else:
            self.take_damage()
                
    def take_damage(self):
        self.character.health -= self.room.enemy.level
        if self.character.health <=3:
            print("low health statement")
        sql = "UPDATE characters SET health=:1 WHERE id=:2"
        CURSOR.execute(sql, (self.character.health,self.character.id))
        print("attack failed language")    
            
    def enemy_defeated(self):
        print(f"You have defeated {self.room.enemy.enemy_name}")
        if self.room.item: 
            self.inventory.add_new_item(self.room.item)
            self.defeated.append(self.room.enemy)             
        points = self.room.enemy.level*100
        self.character.score += points
        
    def score_print_set(self):
        if self.character.high_score < self.score:
            setattr(self.character, "high_score", self.score)
        print(f"Your score is {self.score}")
    
    def update_room(self, id):
        self.room = Room.find_room_by_id(id)

    def is_enemy_defeated(self):
        return self.room.enemy in self.defeated if self.room.enemy else True
    
    