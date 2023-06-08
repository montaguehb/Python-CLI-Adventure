from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({"success": "green", "loot": "yellow", "failure": "red", "neutral":"blue", "character":"bold magenta"})
console = Console(theme=custom_theme)


console.print("Success", style="success")
console.print("Failure", style="failure")
console.print("Loot", style="loot")
console.print("Neutral", style="neutral")
console.print("Character", style="character")


