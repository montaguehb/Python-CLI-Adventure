import sqlite3
import random
from scripts.rooms import Room
from scripts.items import Item
from scripts.enemies import Enemy
from scripts.character import Character
from scripts.inventory import Inventory, CONNECTOR, CURSOR
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme(
    {
        "success": "green",
        "loot": "yellow",
        "failure": "red",
        "neutral": "blue",
        "character": "bold magenta",
    }
)
console = Console(theme=custom_theme)

# CONNECTOR = sqlite3.connect("app/adventure.db")
# CURSOR = CONNECTOR.cursor()


class Floor:
    def __init__(self, inventory):
        self.room = Room.find_room_by_id(1)
        self.defeated = []
        self.character = inventory.character
        self.inventory = inventory
        self.attack_success = []
        self.attack_fail = []
        self.new_monster = []
        self.defeated_enemy = []

    @property
    def defeated_enemy(self):
        return self._defeated_enemy

    @defeated_enemy.setter
    def defeated_enemy(self, enemy):
        with open("./app/txt/defeated.txt", "r") as f:
            self._defeated_enemy = f.read().splitlines()

    @property
    def new_monster(self):
        return self._new_monster

    @new_monster.setter
    def new_monster(self, monster):
        with open("./app/txt/new_monster.txt", "r") as f:
            self._new_monster = f.read().splitlines()

    @property
    def attack_success(self):
        return self._attack_success

    @attack_success.setter
    def attack_success(self, attack_success):
        with open("./app/txt/success.txt", "r") as f:
            self._attack_success = f.read().splitlines()
        # sql = "SELECT * FROM text WHERE used=?"
        # self._attack_success = [text[1] for text in CURSOR.execute(sql, ("success", )).fetchall()]

    @property
    def attack_fail(self):
        return self._attack_fail

    @attack_fail.setter
    def attack_fail(self, attack_fail):
        with open("./app/txt/failure.txt", "r") as f:
            self._attack_fail = f.read().splitlines()

    def enemy_encounter(self):
        print(
            self.new_monster[random.randint(0, len(self.new_monster) - 1)].format(
                enemy_name=self.room.enemy.enemy_name
            )
        )
        console.print(
            f"looks like they are weak agaist {self.enemy_weaknesses()}",
            style="character",
        )
        if len(self.enemy_weaknesses()) > 1:
            print("the order is important")

    def enemy_weaknesses(self):
        sql = "SELECT item_description FROM items WHERE item_name=?"
        return [
            CURSOR.execute(sql, (mechanic,)).fetchone()[-1]
            for mechanic in self.room.enemy.fight_mechanics
        ]

    def enemy_attack_response(self):
        console.print(
            "the enemy name is getting closer. Attack again!", style="character"
        )
        console.print(f"it's weak against {self.enemy_weaknesses()}", style="character")

    def attack(self, attack):
        enemy = self.room.enemy
        inventory_names = (item.item_name for item in self.inventory.items)
        if attack in inventory_names and attack == enemy.fight_mechanics[0]:
            enemy.fight_mechanics.pop(0)
            console.print(
                self.attack_success[
                    random.randint(0, len(self.attack_success) - 1)
                ].format(enemy_name=self.room.enemy.enemy_name, item_name=attack),
                style="success",
            )
            if not enemy.fight_mechanics:
                self.enemy_defeated()
        else:
            self.take_damage(attack)

    def take_damage(self, attack):
        self.character.health -= self.room.enemy.level
        if self.character.health <= 3:
            console.print(
                f"{self.character.username}, your health has diminished quickly.  Tread carefully for the next encounter may prove to be your last!",
                style="failure",
            )
        sql = "UPDATE characters SET health=:1 WHERE id=:2"
        CURSOR.execute(sql, (self.character.health, self.character.id))
        console.print(
            self.attack_fail[random.randint(0, len(self.attack_fail) - 1)].format(
                attack=attack,
                enemy_lvl=self.room.enemy.level,
                item_name=attack,
                enemy_name=self.room.enemy.enemy_name,
            ),
            style="failure",
        )

    def enemy_defeated(self):
        console.print(
            self.defeated_enemy[random.randint(0, len(self.defeated_enemy) - 1)].format(
                enemy_name=self.room.enemy.enemy_name
            ),
            style="success",
        )
        if self.room.item:
            self.inventory.add_new_item(self.room.item)
            self.defeated.append(self.room.enemy)
        points = self.room.enemy.level * 100
        self.character.score += points

    def score_print_set(self):
        if self.character.high_score < self.score:
            setattr(self.character, "high_score", self.score)
        console.print(f"Your score is {self.score}", style="character")

    def update_room(self, id):
        self.room = Room.find_room_by_id(id)

    def is_enemy_defeated(self):
        return self.room.enemy in self.defeated if self.room.enemy else True

    def game_complete(self):
        print("you beat the game")
        print(f"Your Score: {self.score}")
        self.high_score_print()

    def high_score_print(self):
        print("High Scores:")
        print(
            CURSOR.execute(
                "SELECT username, highest_score FROM characters LIMIT 5 ORDER BY highest_score DESC"
            )
        )
