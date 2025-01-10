import sys
from todo_list import TodoList

def print_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Clear all tasks")
    print("5. Delete a task")
    print("6. Edit a task")
    print("7. Exit")

def add_task(todo_list):
    task_name = input("Enter the task name: ")
    todo_list.add_task(task_name)
    print(f"Task '{task_name}' added.")

def list_tasks(todo_list):
    tasks = todo_list.list_tasks()
    if tasks:
        print("\nTasks:")
        for task in tasks:
            print(f"- {task['name']} [{task['status']}]")
    else:
        print("No tasks found.")

def mark_task_completed(todo_list):
    task_name = input("Enter the task name to mark as completed: ")
    todo_list.mark_task_as_completed(task_name)
    print(f"Task '{task_name}' marked as completed.")

def clear_tasks(todo_list):
    todo_list.clear_tasks()
    print("All tasks have been cleared.")

def delete_task(todo_list):
    task_name = input("Enter the task name to delete: ")
    todo_list.delete_task(task_name)
    print(f"Task '{task_name}' deleted.")

def edit_task(todo_list):
    old_name = input("Enter the current name of the task: ")
    new_name = input("Enter the new name for the task: ")
    todo_list.edit_task(old_name, new_name)
    print(f"Task '{old_name}' renamed to '{new_name}'.")

def main():
    todo_list = TodoList()

    while True:
        print_menu()

        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            list_tasks(todo_list)
        elif choice == '3':
            mark_task_completed(todo_list)
        elif choice == '4':
            clear_tasks(todo_list)
        elif choice == '5':
            delete_task(todo_list)
        elif choice == '6':
            edit_task(todo_list)
        elif choice == '7':
            print("Exiting the program.")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
