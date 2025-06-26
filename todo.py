todo_list = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list):
            status = "✅" if task["done"] else "❌"
            print(f"{i+1}. {task['task']} [{status}]")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "done": False})
    print("Task added!")

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(todo_list):
            todo_list[num-1]["done"] = True
            print("Marked as done!")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num-1)
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number.")
    except:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! 🫡")
        break
    else:
        print("Invalid choice. Try again.")
