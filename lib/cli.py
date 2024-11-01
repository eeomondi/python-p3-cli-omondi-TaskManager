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
    click.echo(f'User "{name}" added.')

@cli.command()
def list_users():
    """List all users."""
    db = SessionLocal()
    users = db.query(User).all()
    if not users:
        click.echo("No users found.")
    for user in users:
        click.echo(f'User ID: {user.id}, Name: {user.name}')

@cli.command()
@click.option('--title', prompt='Task Title', help='Title of the task.')
@click.option('--user_id', prompt='User ID', type=int, help='ID of the user assigned to the task.')
def add_task(title, user_id):
    """Add a new task."""
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        click.echo(f"User ID {user_id} does not exist. Task not added.")
        return
    new_task = Task(title=title, user_id=user_id)
    db.add(new_task)
    db.commit()
    click.echo(f'Task "{title}" added for User ID {user_id}.')

@cli.command()
def list_tasks():
    """List all tasks."""
    db = SessionLocal()
    tasks = db.query(Task).all()
    if not tasks:
        click.echo("No tasks found.")
    for task in tasks:
        click.echo(f'Task ID: {task.id}, Title: {task.title}, User ID: {task.user_id}')

@cli.command()
@click.option('--user_id', prompt='User ID', type=int, help='ID of the user to delete.')
def delete_user(user_id):
    """Delete a user."""
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        click.echo(f'User ID {user_id} deleted.')
    else:
        click.echo(f'User ID {user_id} not found.')

@cli.command()
@click.option('--task_id', prompt='Task ID', type=int, help='ID of the task to delete.')
def delete_task(task_id):
    """Delete a task."""
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        click.echo(f'Task ID {task_id} deleted.')
    else:
        click.echo(f'Task ID {task_id} not found.')

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo('Database initialized.')

if __name__ == '__main__':
    cli()
