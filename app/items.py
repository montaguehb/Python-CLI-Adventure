import sqlite3

CONNECTER = sqlite3.connect('app/adventure.db')
CURSOR = CONNECTER.cursor()

class Item():
    def __init__(self, **kwargs):
        pass 