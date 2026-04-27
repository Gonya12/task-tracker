import tkinter as tk
from tkinter import messagebox
import backend

# Make sure database/table exists
backend.create_table()

# Create window
root = tk.Tk()
root.title("Task Tracker")
root.geometry("400x400")

# Input field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Load tasks into listbox
def load_tasks():
    listbox.delete(0, tk.END)
    tasks = backend.get_all_tasks()

    for task in tasks:
        # task = (id, task_name, status)
        listbox.insert(tk.END, f"{task[0]} | {task[1]} - {task[2]}")

# Add task
def add_task():
    task = entry.get()
    success, message = backend.add_task(task)

    if success:
        entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", message)

# Mark complete
def complete_task():
    selected = listbox.curselection()
    if selected:
        task = backend.get_all_tasks()[selected[0]]
        task_id = task[0]

        success, message = backend.mark_task_completed(task_id)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task")

# Delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        task = backend.get_all_tasks()[selected[0]]
        task_id = task[0]

        success, message = backend.delete_task(task_id)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task")

# Buttons
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

complete_btn = tk.Button(root, text="Mark Complete", command=complete_task)
complete_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

# Initial load
load_tasks()

# Run app
root.mainloop()