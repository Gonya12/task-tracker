# Task Tracker

This is a simple task tracker application built using Python, Tkinter, and SQLite. The goal of this project is to create an easy way for users to keep track of their daily tasks without using complicated apps.

---

## Team Members

- Briana Randolph — worked on the GUI using Tkinter  
- Gonzalo Leon Carlos — worked on the backend and database  

---

## What the app does

The application lets users:

- Add new tasks  
- See all their tasks  
- Mark tasks as completed  
- Delete tasks  

All the tasks are saved in a database, so they stay even after closing the app.

---

## How it works

The backend uses SQLite to store the tasks. Each task has:
- an ID
- a name
- a status (Pending or Completed)

The program uses basic CRUD operations:
- Create → add a task  
- Read → show tasks  
- Update → mark as completed  
- Delete → remove a task  

---

## How to run

1. Open the project folder  
2. Run:

```bash
python backend.py