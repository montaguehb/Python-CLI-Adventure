import sqlite3
from scripts.character import Character
from scripts.items import Item
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
CONNECTOR = sqlite3.connect("app/adventure.db")
CURSOR = CONNECTOR.cursor()


class Inventory:
    def __init__(self, character=None):
        self.character = character
        self.items = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if not hasattr(self, "_id") and isinstance(id, int):
            self._id = id
        else:
            raise AttributeError("id is immutable and must be of type int")

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, character):
        if isinstance(character, Character):
            self._character = character
        else:
            raise AttributeError

    def add_new_item(self, item):
        if isinstance(item, Item):
            self.items.append(item)
            self.update_new_inventory_db(item)
            console.print(
                f"""Your spoils include {item.item_name}. 
                  This {item.item_name} can be used to {item.item_description} and may prove useful in your next encounter.""",
                style="loot",
            )
        else:
            raise AttributeError("item must be of type Item")

    def update_new_inventory_db(self, item):
        sql = "INSERT INTO inventory (character_id, item_id) VALUES(?, ?)"
        CURSOR.execute(sql, (self.character.id, item.id))
        CONNECTOR.commit()

    def pull_existing_inventory(self):
        sql = "SELECT * from inventory"
        inventory = CURSOR.execute(sql).fetchone()
        self.items.append(Item.find_by_id(inventory[2]))
