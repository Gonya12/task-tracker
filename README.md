# Task Tracker Application

A simple desktop-based task management application built using Python, Tkinter, and SQLite. This application allows users to organize and manage their daily tasks in an efficient and user-friendly way.

---

## 👥 Team Members

- **Briana Randolph** — GUI Design and Tkinter Interface  
- **Gonzalo Leon Carlos** — Backend Development and Database Integration  

---

## 🎯 Project Overview

The Task Tracker Application is designed to help users manage daily responsibilities such as school assignments, work tasks, and personal goals.

Many existing task management tools are complex and difficult to use. This project focuses on providing a simple, lightweight, and easy-to-use solution.

Users can:
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks

All data is stored in a database, allowing tasks to persist even after closing the application.

---

## ⚙️ Features

- Add new tasks  
- View all existing tasks  
- Mark tasks as completed  
- Delete tasks  
- Persistent storage using SQLite  

---

## 🛠️ Technologies Used

- Python  
- Tkinter (GUI)  
- SQLite (Database)  
- Git & GitHub  

---

## 🗄️ Database Structure

The application uses SQLite with a table named `tasks`:

| Column Name | Type    | Description                  |
|------------|--------|------------------------------|
| id         | INTEGER | Unique task ID (Primary Key) |
| task_name  | TEXT    | Name of the task             |
| status     | TEXT    | Task status (Pending/Completed) |

---

## 🔄 CRUD Operations

- **Create** → Add new tasks  
- **Read** → Display all tasks  
- **Update** → Mark tasks as completed  
- **Delete** → Remove tasks  

---

## 🧠 My Contribution (Gonzalo)

My role focused on backend development and database integration.

I:
- Designed and created the SQLite database
- Implemented CRUD operations in Python
- Developed functions to handle task storage, retrieval, updates, and deletion
- Tested the backend to ensure all functionality works correctly

---

## ▶️ How to Run the Project

1. Open the project folder in VS Code or terminal  
2. Run the backend setup:

```bash
python backend.py