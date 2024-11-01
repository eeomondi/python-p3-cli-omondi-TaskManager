import click
from database import init_db, SessionLocal
from models import User

@click.group()
def cli():
    """Task Manager CLI."""
    pass

@cli.command()
@click.option('--name', prompt='User Name', help='Name of the user.')
def add_user(name):
    """Add a new user."""
    db = SessionLocal()
    new_user = User(name=name)
    db.add(new_user)
    db.commit()
    click.echo(f'User {name} added.')

@cli.command()
def list_users():
    """List all users."""
    db = SessionLocal()
    users = db.query(User).all()
    for user in users:
        click.echo(f'User ID: {user.id}, Name: {user.name}')

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo('Database initialized.')

if __name__ == '__main__':
    cli()
