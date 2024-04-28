tasks = []

def add_task():
    task_name = input("Enter task name: ")
    task_deadline = input("Enter task deadline: ")
    tasks.append({"Task": task_name, "Deadline": task_deadline})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['Task']} - Deadline: {task['Deadline']}")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("What do you want to do: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        pass  # To be implemented: delete task functionality
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select ask valid option.")
