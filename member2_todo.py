from member1_todo import load_tasks, save_tasks, add_task, view_tasks


# Mark task as done
def mark_done(tasks):

    task_id = int(input("Enter task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print("Task marked as done")
            return

    print("Task not found")


# Delete a task
def delete_task(tasks):

    task_id = int(input("Enter task ID: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

            for i, task in enumerate(tasks):
                task["id"] = i + 1

            save_tasks(tasks)

            print("Task deleted")
            return

    print("Task not found")


# Filter tasks
def filter_tasks(tasks):

    status = input("Show 'pending' or 'done': ")

    filtered = [task for task in tasks if task["status"] == status]

    for task in filtered:
        print(f"{task['id']} | {task['title']}")


# Main menu
def main():

    tasks = load_tasks()

    while True:

        print("\n=== TO DO LIST MANAGER ===")
        print("1 Add Task")
        print("2 View Tasks")
        print("3 Mark Task as Done")
        print("4 Delete Task")
        print("5 Filter Tasks")
        print("6 Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_done(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            filter_tasks(tasks)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


main()