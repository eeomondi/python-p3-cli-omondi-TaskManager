import click
from database import get_session
from models import Project, Task, Base

@click.group()
def cli():
    """A simple task manager CLI."""
    pass

@cli.command()
@click.argument('name')
def add_project(name):
    """Add a new project."""
    session = get_session()
    project = Project(name=name)
    session.add(project)
    session.commit()
    click.echo(f"Added project: {project.name}")

@cli.command()
def list_projects():
    """List all projects."""
    session = get_session()
    projects = session.query(Project).all()
    for project in projects:
        click.echo(f"Project ID: {project.id}, Name: {project.name}")

@cli.command()
@click.argument('project_id')
@click.argument('title')
def add_task(project_id, title):
    """Add a new task to a project."""
    session = get_session()
    task = Task(title=title, project_id=project_id)
    session.add(task)
    session.commit()
    click.echo(f"Added task: {task.title} to project ID: {project_id}")

@cli.command()
@click.argument('project_id')
def list_tasks(project_id):
    """List all tasks for a project."""
    session = get_session()
    tasks = session.query(Task).filter(Task.project_id == project_id).all()
    for task in tasks:
        click.echo(f"Task ID: {task.id}, Title: {task.title}")

def main():
    Base.metadata.create_all(get_engine())
    cli()

if __name__ == '__main__':
    main()
