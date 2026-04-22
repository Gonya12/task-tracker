import sqlite3

DB_NAME = "tasks.db"


def connect_db():
    """
    Connect to the SQLite database.
    """
    return sqlite3.connect(DB_NAME)


def create_table():
    """
    Create the tasks table if it does not already exist.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()


def add_task(task_name):
    """
    Add a new task to the database.
    """
    if not task_name.strip():
        return False, "Task name cannot be empty."

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tasks (task_name, status)
        VALUES (?, ?)
    """, (task_name.strip(), "Pending"))

    conn.commit()
    conn.close()

    return True, "Task added successfully."


def get_all_tasks():
    """
    Retrieve all tasks from the database.
    Returns a list of tuples: (id, task_name, status)
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, task_name, status
        FROM tasks
        ORDER BY id ASC
    """)

    tasks = cursor.fetchall()
    conn.close()

    return tasks


def mark_task_completed(task_id):
    """
    Update a task's status to Completed.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = 'Completed'
        WHERE id = ?
    """, (task_id,))

    if cursor.rowcount == 0:
        conn.close()
        return False, "Task not found."

    conn.commit()
    conn.close()

    return True, "Task marked as completed."


def delete_task(task_id):
    """
    Delete a task from the database.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))

    if cursor.rowcount == 0:
        conn.close()
        return False, "Task not found."

    conn.commit()
    conn.close()

    return True, "Task deleted successfully."


def get_task_by_id(task_id):
    """
    Retrieve one task by its ID.
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, task_name, status
        FROM tasks
        WHERE id = ?
    """, (task_id,))

    task = cursor.fetchone()
    conn.close()

    return task


if __name__ == "__main__":
    create_table()
    print("Database and table are ready.")