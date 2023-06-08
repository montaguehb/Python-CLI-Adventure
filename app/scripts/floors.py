import sqlite3
from scripts.rooms import Room
from scripts.items import Item
from scripts.enemies import Enemy
from scripts.character import Character
from scripts.inventory import Inventory

CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()


class Floor:
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

    def enemy_encounter(self):
        print(f"oh look a bad guy")
        print(f"looks like they are weak agaist {self.enemy_weaknesses()}")
        if len(self.enemy_weaknesses()) > 1:
            print("the order is important")

    def enemy_weaknesses(self):
        sql = "SELECT item_description FROM items WHERE item_name=?"
        return [
            CURSOR.execute(sql, (mechanic,)).fetchone()[-1]
            for mechanic in self.room.enemy.fight_mechanics
        ]

    def enemy_attack_response(self):
        print("the enemy name is getting closer. Attack again!")
        print(f"it's weak against {self.enemy_weaknesses()}")

    def attack(self, input):
        enemy = self.room.enemy
        inventory_names = (item.item_name for item in self.inventory)
        if input in inventory_names and input == enemy.fight_mechanics[0]:
            enemy.fight_mechanics.pop(0)
            print("attack success language")
            if not enemy.fight_mechanics:
                self.enemy_defeated()
        else:
            self.take_damage()

    def take_damage(self):
        self.character.health -= self.room.enemy.level
        if self.character.health <= 3:
            print("low health statement")
        sql = "UPDATE characters SET health=:1 WHERE id=:2"
        CURSOR.execute(sql, (self.character.health, self.character.id))
        print("attack failed language")

    def enemy_defeated(self):
        print(f"You have defeated {self.room.enemy.enemy_name}")
        if self.room.item:
            self.inventory.add_new_item(self.room.item)
            self.defeated.append(self.room.enemy)
        points = self.enemy.level * 100
        self.score += points

    def score_print_set(self):
        if self.character.highest_score < self.score:
            setattr(self.character, "highest_score", self.score)
            sql = "UPDATE characters SET highest_score=:1, WHERE id=:2"
            CURSOR.execute(sql, (self.character.highest_score, self.character.id))
        print(f"Your score is {self.score}")

    def highest_scores_print():
        print("High Scores:")
        CURSOR.execute(
            "SELECT username, highest_score FROM characters LIMIT 5 ORDER BY highest_score DESC "
        )

    def game_complete(self):
        print("game success!")
        self.score_print_set()
        self.highest_scores_print()
