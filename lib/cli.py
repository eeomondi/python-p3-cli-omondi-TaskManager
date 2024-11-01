import click
from models import Project, Task
from database import SessionLocal, init_db

init_db()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Project name', help='Name of the project.')
def create_project(name):
    db = SessionLocal()
    project = Project(name=name)
    db.add(project)
    db.commit()
    click.echo(f'Project "{name}" created!')

@cli.command()
def list_projects():
    db = SessionLocal()
    projects = db.query(Project).all()
    for project in projects:
        click.echo(f'Project ID: {project.id}, Name: {project.name}')

@cli.command()
@click.argument('project_id', type=int)
def delete_project(project_id):
    db = SessionLocal()
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
        click.echo(f'Project ID {project_id} deleted.')
    else:
        click.echo(f'Project ID {project_id} not found.')

# Similar commands for Task...

if __name__ == "__main__":
    cli()
