import click
from database import init_db, SessionLocal
from models import User, Task

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
@click.option('--title', prompt='Task Title', help='Title of the task.')
@click.option('--user_id', prompt='User ID', type=int, help='ID of the user assigned to the task.')
def add_task(title, user_id):
    """Add a new task."""
    db = SessionLocal()
    new_task = Task(title=title, user_id=user_id)
    db.add(new_task)
    db.commit()
    click.echo(f'Task "{title}" added for User ID {user_id}.')

@cli.command()
def list_tasks():
    """List all tasks."""
    db = SessionLocal()
    tasks = db.query(Task).all()
    for task in tasks:
        click.echo(f'Task ID: {task.id}, Title: {task.title}, User ID: {task.user_id}')

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo('Database initialized.')

if __name__ == '__main__':
    cli()

