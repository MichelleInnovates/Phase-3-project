import click
from .database import create_tables, drop_tables

@click.group()
def cli():
    pass

@cli.command()
def create_tables():
    create_tables()
    click.echo("Tables created successfully.")

@cli.command()
def drop_tables():
    drop_tables()
    click.echo("Tables dropped successfully.")

if __name__ == '__main__':
    cli()
