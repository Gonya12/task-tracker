from backend import (
    create_table,
    add_task,
    get_all_tasks,
    mark_task_completed,
    delete_task,
    get_task_by_id
)


def print_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nCurrent Tasks:")
        for task in tasks:
            print(f"ID: {task[0]} | Task: {task[1]} | Status: {task[2]}")
    print("-" * 40)


def main():
    create_table()

    print("Testing backend...\n")

    # Add tasks
    print(add_task("Finish Python project"))
    print(add_task("Study for exam"))
    print(add_task("Buy groceries"))

    print_tasks()

    # Mark task completed
    print(mark_task_completed(1))
    print_tasks()

    # Get one task
    task = get_task_by_id(1)
    print("Task with ID 1:", task)
    print("-" * 40)

    # Delete task
    print(delete_task(2))
    print_tasks()


if __name__ == "__main__":
    main()