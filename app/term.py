import click
import sys
from scripts import *

stdin = click.get_text_stream("stdin")

def main():
    character = start()
    game(character)
    
def start():
    click.echo("Do you want to create a new character or use and old character")
    return char_type()

def create_new_char():
    new_char = None
    while not new_char:
        name = click.prompt("What is the name of your character", type=str)
        check_exit(name)
        if not character.Character.find_by_username(name):
            new_char = character.Character(username=name)
            new_char.add_to_db()
            return new_char
        else:
            click.echo("User already exists")

def game(character):
    pass

def old_char():
    old_char = None
    while not old_char:
        name = click.prompt("What is the name of your character", type=str)
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
        if user_type == 'y':
            return create_new_char()
        elif user_type == 'n':
            return old_char()
               
def check_exit(string):
    if string == ".exit":
        sys.exit()
        
if __name__ == "__main__":
    main()
        