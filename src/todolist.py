import tkinter as tk
import json

# Function to load tasks from file
def load_tasks():
    try:
        with open('src/tasks.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open('src/tasks.json', 'w') as file:
        json.dump(tasks, file)

# Function to add task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        entry.delete(0, tk.END)
        update_listbox()

# Function to update listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to delete task
def delete_task():
    selected = listbox.curselection()
    if selected:
        del tasks[selected[0]]
        save_tasks(tasks)
        update_listbox()

# Main application
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")

# Load tasks
tasks = load_tasks()

# Create and place widgets
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Update listbox
update_listbox()

# Start the main event loop
root.mainloop()