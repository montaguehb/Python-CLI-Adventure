import click
from app.scripts.character import Character

@click.command()
@click.option('--name', prompt=True)
def hello(name):
    click.echo(f"Hello {name}!")