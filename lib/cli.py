import click
from lib.db import models
from lib.db.database import Session

@click.group()
def cli():
    pass

@cli.command()
def create_tables():
    models.Base.metadata.create_all(bind=Session.get_bind())
    click.echo("Tables created successfully.")

@cli.command()
def drop_tables():
    models.Base.metadata.drop_all(bind=Session.get_bind())
    click.echo("Tables dropped successfully.")

if __name__ == '__main__':
    cli()