# Python-CLI-Adventure

What is it?

Pythonic is a CLI text-based adventure game to help you learn GitHub commands.

Pythonic by Histrenyan, is an action packed adventure game hosted right in your very own computer terminal. In this CLI text-based adventure game, you'll find yourself in a Graveyard battling demons attempting to rule the world, one Git

Install

$ git clone git@github.com:montaguehb/Python-CLI-Adventure.git
$ pipenv install
$ python3 ./app/term.py

Usage

At run, you'll be guided on character creation. Basic navigation from room to room via north, south, east, and west commands as well as battle using your inventory that can be called on by item name.

Exit

.exit from any prompt to quit the program

Items

Here's a short list of the types of items you'll be able to collect.

add - Stages file changes to be committed Base weapon
commit - Commits the staged changes to the repo Base weapon
init - Initializes an empty git repo Base weapon
log - View all commits to a repo Info
status - See a summary of staged changes Info
diff - View changes to be committed Base weapon
branch - lists all existing branches Info
switch - switch to another branch

Enemies

You can attack enemies using the above items once you've acquired them. Here's some examples of the enemies and the attacks you'd use to take them out.

git abomination - branch, show
git revenant - init, add
git scorpion - log
git pest - status
