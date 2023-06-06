import click
# from scripts.character import Character

@click.command()
@click.option('--name', prompt=True)
def hello(name):
    click.echo(f"Hello {name}!")

if __name__ == "__main__":
    hello()