# python-p3-cli-omondi-TaskManager

## Task Manager CLI Application

## Overview

A simple command line interface to manage tasks categorized by different categories.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Run `pipenv install` to set up the environment.
4. Run `python cli.py` to start the application.

## Features

- Add projects
- View all projects
- Add tasks to projects
- List all task for a specific project 

## Running your Application

1. **Initialize the database:**

   When you first run the application, it will create the database and tables.

2. **Start the CLI:**

   ```bash
   pipenv run python cli.py

3. Demo Commands:

    - Add a project: add_project "Project 1"
    - List projects: list_projects
    - Add a task: add_task 1 "Task 1"
    - List tasks: list_tasks 1
