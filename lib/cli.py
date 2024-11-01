import sys
from lib.database import Session
from models import Task, Category

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(session):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category_name = input("Enter category name: ")

    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()

    task = Task(title=title, description=description, category=category)
    session.add(task)
    session.commit()
    print("Task added!")

def view_tasks(session):
    tasks = session.query(Task).all()
    for task in tasks:
        print(f"{task.id}: {task.title} - {task.description} [Category: {task.category.name}]")

def delete_task(session):
    task_id = int(input("Enter task ID to delete: "))
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print("Task deleted!")
    else:
        print("Task not found.")

def main():
    session = Session()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(session)
        elif choice == '2':
            view_tasks(session)
        elif choice == '3':
            delete_task(session)
        elif choice == '4':
            session.close()
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
