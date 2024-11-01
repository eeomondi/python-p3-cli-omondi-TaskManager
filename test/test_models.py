import pytest
from sqlalchemy.orm import sessionmaker
from database import engine, init_db, SessionLocal
from models import Project, Task

# Set up the database
@pytest.fixture(scope='module')
def test_db():
    init_db()
    yield SessionLocal()
    SessionLocal().close()

def test_create_project(test_db):
    project = Project(name="Test Project")
    test_db.add(project)
    test_db.commit()
    assert project.id is not None

def test_create_task(test_db):
    project = Project(name="Another Project")
    test_db.add(project)
    test_db.commit()
    task = Task(title="Test Task", project_id=project.id)
    test_db.add(task)
    test_db.commit()
    assert task.id is not None
    assert task.project_id == project.id
