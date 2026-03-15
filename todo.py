FILE_NAME = "tasks.txt"

# load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                id, title, status = line.strip().split(",")
                tasks.append({
                    "id": int(id),
                    "title": title,
                    "status": status
                })
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['id']},{task['title']},{task['status']}\n")

# Add a new task
def add_task(tasks):
    title = input(f"Enter task title: ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "status": "pending"
    }
    tasks.append(task)
    save_tasks(tasks)

    print(f"Task added successfully!")

# View all tasks
def view_tasks(tasks):

    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\nID | STATUS| TASK")
    print("----------------------")

    for task in tasks:
        print(f"{task['id']} | {task['title']} | {task['status']}")
