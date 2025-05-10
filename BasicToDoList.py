tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
    else:
        print("Invalid task number.")

def view_tasks():
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i + 1}. {task['task']} [{status}]")

while True:
    print("\n 1.Add Task\n 2.Complete Task\n 3.View Tasks\n 4.Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
        index = int(input("Enter task number to mark as complete: ")) - 1
        complete_task(index)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
