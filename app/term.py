import click
import sys
import random
from scripts import *
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme(
    {
        "success": "green",
        "loot": "yellow",
        "failure": "red",
        "neutral": "blue",
        "character": "bold magenta",
        "starting": "bold cyan",
    }
)
console = Console(theme=custom_theme)

stdin = click.get_text_stream("stdin")


def main():
    character = start()
    game(character)


def start():
    console.print(read_("./app/txt/welcome.txt"), style="starting")
    return char_type()


def create_new_char():
    new_char = None
    while not new_char:
        name = click.prompt("name", type=str).lower()
        check_exit(name)
        if not character.Character.find_by_username(name):
            new_char = character.Character(username=name)
            new_char.add_to_db()
            return new_char
        else:
            console.print("User already exists", style="failure")


def game(character):
    inv = inventory.Inventory(character)
    floor = floors.Floor(inventory=inv)
    boss = enemies.Enemy.find_enemy_by_id(1)
    while boss.enemy_name not in (enemy.enemy_name for enemy in floor.defeated):
        console.print(f"{floor.room.room_text()}", style="neutral")
        playing = combat(inv, floor, character)
        if not floor.room.enemy and floor.room.item:
            floor.inventory.add_new_item(floor.room.item)
        move(floor)
        if not playing:
            return playing
    end()
    return False


def old_char():
    old_char = None
    while not old_char:
        name = click.prompt("What is the name of your character", type=str).lower()
        check_exit(name)
        old_char = character.Character.find_by_username(name)
        if old_char:
            return old_char
        else:
            console.print("User does not exist", style="failure")


def char_type():
    user_type = ""
    while user_type not in ("y", "n"):
        console.print(f"Please input one of these values {['y','n']}", style="neutral")
        user_type = click.prompt("New character", type=str).lower()
        check_exit(user_type)
        console.print(
            "Before you venture forward, what is your name my brave soul?",
            style="neutral",
        )
        if user_type == "y":
            return create_new_char()
        elif user_type == "n":
            return old_char()


def check_exit(string):
    if string == ".exit":
        console.print(
            """It appears your logic is no match for the treacherous beasts of the Git Graveyard!
                    We are not surprised as the Git Graveyard is no place for the faint of heart!""",
            style="failure",
        )
        sys.exit()


def combat(inventory, floor, character):
    if floor.is_enemy_defeated():
        return True
    floor.enemy_encounter()
    while character.health > 0 and floor.room.enemy.fight_mechanics:
        attack = click.prompt("Attack", type=str)
        check_exit(attack)
        show_commands() if attack == "git" else floor.attack(attack)
    if character.health <= 0:
        return game_over(floor.room.enemy.enemy_name, character)
    return True


def move(floor):
    directions = [key for key, value in floor.room.directions.items() if value > 0]
    direction = ""
    console.print(
        f"Which direction do you want to move {directions}", style="character"
    )
    while direction not in directions:
        direction = click.prompt("Direction", type=str).lower()
        check_exit(direction)
        if direction in directions:
            floor.update_room(floor.room.directions[direction])
            console.print(
                f"You move {direction}",
                style="neutral",
            )
        elif direction == "git":
            show_commands(floor)
        else:
            console.print("Please input a valid direction", style="failure")


def game_over(enemy_name, character):
    click.echo(read_("./app/txt/game_over.txt").format(enemy_name=enemy_name))
    repeat = ""
    while repeat not in ("y", "n"):
        repeat = click.prompt("play again?", type=str)
        check_exit(repeat)
        if repeat == "y":
            with open("./app/txt/try_again.txt", "r") as file:
                text = file.read().splitlines()
                console.print(
                    text[random.randint(0, len(text) - 1)].format(
                        username=character.username
                    ),
                    style="success",
                )
            return True
        elif repeat == "n":
            return False


def end():
    click.echo("end")


def show_commands(floor):
    console.print(floor.inventory.items, style="loot")


def read_(file):
    with open(file, "r") as file:
        return file.read()


if __name__ == "__main__":
    playing = True
    while playing:
        playing = main()
