import json

# Load data
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = {}

def add_task():
    task = input("Enter Task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    if task in tasks:
        print("Task already exists!")
        return

    tasks[task] = {
        "status": "Pending"
    }

    print("Task Added Successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No Tasks Found")
        return

    print("\n===== TASK LIST =====")
    for task, details in tasks.items():
        print(f"Task   : {task}")
        print(f"Status : {details['status']}")
        print("-" * 25)


def mark_all_tasks():
    for task in tasks:
        tasks[task]["status"] = "Completed"

    print("All tasks completed")

def mark_one_task():
    task = input("Enter the task name:")
    if task in tasks:
        tasks[task]["status"] = "Completed"
        print("Task is marked Completed")

def delete_task():
    task = input ("Enter the name of the task you wanna delete :")
    if task in tasks:
        warning = input("Are you sure you wanna delete that task :(yes/no) :")
        if warning.lower() == "yes":
        

            del tasks[task]
            print("Task Have been deleted")
        
        else:
            print("Task has not been deleted")
    
        
while True:
    print("\n===== TO DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark All Task")
    print("4. Mark One Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        mark_all_tasks()

    elif choice == "4":
        mark_one_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        print("Tasks Saved Successfully!")
        print("Goodbye!")
        break

    else:
        print("Invalid Choice! Please try again.")