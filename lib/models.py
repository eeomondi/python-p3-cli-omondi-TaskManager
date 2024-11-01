from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="project")

    def __repr__(self):
        return f"<Project(name={self.name})>"

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task(title={self.title}, project_id={self.project_id})>"
