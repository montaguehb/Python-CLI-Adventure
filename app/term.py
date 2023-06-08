import click
import sys
from scripts import *

stdin = click.get_text_stream("stdin")

def main():
    character = start()
    click.echo(f"Welcome {character.username}")
    game(character)
    
def start():
    click.echo(read("./app/txt/welcome.txt"))
    return char_type()

def create_new_char():
    new_char = None
    while not new_char:
        name = click.prompt("name", type=str)
        check_exit(name)
        if not character.Character.find_by_username(name):
            new_char = character.Character(username=name)
            new_char.add_to_db()
            return new_char
        else:
            click.echo("User already exists")

def game(character):
    inv = inventory.Inventory(character)
    floor = floors.Floor(inventory=inv)
    boss = enemies.Enemy.find_enemy_by_id(1)
    while boss not in floor.defeated:
        click.echo(f"{floor.room.room_text()}")
        combat(inv, floor, character)
        if not floor.room.enemy and floor.room.item:
            floor.inventory.add_new_item(floor.room.item)
        move(floor)
    
def old_char():
    old_char = None
    while not old_char:
        name = click.prompt("What is the name of your character", type=str).lower()
        check_exit(name)
        old_char = character.Character.find_by_username(name)
        if old_char:
            return old_char
        else:
            click.echo("User does not exist") 

def char_type():
    user_type = ""
    while user_type not in ("y", "n"):
        click.echo("Please input one of these values [yn]")
        user_type = click.prompt("New character", type=str).lower()
        check_exit(user_type)
        click.echo("Before you venture forward, what is your name my brave soul?")
        if user_type == 'y':
            return create_new_char()
        elif user_type == 'n':
            return old_char()
               
def check_exit(string):
    if string == ".exit":
        sys.exit()

def combat(inventory, floor, character):
    if floor.is_enemy_defeated():
        return
    floor.enemy_encounter()
    while character.health > 0 and floor.room.enemy.fight_mechanics:
        attack = click.prompt("Attack", type=str)
        check_exit(attack)
        floor.attack(attack)    
    if character.health <= 0:
        game_over()    
                       
def move(floor):
    directions = [key for key, value in floor.room.directions.items() if value > 0]
    direction = ""
    # room = click.prompt("room [yn]", type=str)
    # if room == "y":
    #     room_id = click.prompt("room_id", type=int)
    #     floor.update_room(room_id)  
    # else:
    click.echo(f"Which direction do you want to move {directions}")
    while direction not in directions:
        direction = click.prompt("Direction", type=str).lower()
        check_exit(direction)
        if direction in directions:
            floor.update_room(floor.room.directions[direction])
            click.echo(f"You move {direction} and find yourself in insert floor directions")
        else:
            click.echo("Please input a valid direction")

def game_over():
    sys.exit()
    # repeat = click.prompt("play again?", type=str)
    # check_exit(repeat)

def show_commands(command):
    pass

def read(file):
    with open(file, "r") as file:
        return file.read()
                   
if __name__ == "__main__":
    main()
        