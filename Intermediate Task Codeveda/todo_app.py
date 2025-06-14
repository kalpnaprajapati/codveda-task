import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="todo_app"
)
cursor = conn.cursor()

def add_task():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task")

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        task_id = listbox.get(selected_task)[0]
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        load_tasks()
    else:
        messagebox.showwarning("Warning", "You must select a task")

def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        listbox.insert(tk.END, (task[0], task[1]))

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=20)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

load_tasks()
root.mainloop()

