# import tkinter as tk

# # Create the main application window
# root = tk.Tk()
# root.title("Tkinter Project Template")
# root.geometry("400x300")

# # Function to handle button click
# def on_button_click():
#     user_input = entry.get()
#     label.config(text=f"You entered: {user_input}")

# # Create and place widgets
# label = tk.Label(root, text="Enter something:")
# label.pack(pady=10)

# entry = tk.Entry(root, width=30)
# entry.pack(pady=5)

# button = tk.Button(root, text="Submit", command=on_button_click)
# button.pack(pady=10)

# # Start the main event loop
# root.mainloop()
# src/main.py
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Try to load existing file, otherwise use default
TASK_FILE = "todolist_data.json"
DEFAULT_TASKS = [
    {"title": "Review Code Submission", "status": "pending"},
    {"title": "Complete Project Report", "status": "in_progress"},
    {"title": "Buy Groceries", "status": "done"}
]

def save_tasks(tasks):
    """Saves tasks to JSON file."""
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    """Loads tasks from JSON file or returns default if not found."""
    if os.path.exists(TASK_FILE):
        try:
            with open(TASK_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return DEFAULT_TASKS

def handle_status_change(status_type):
    """
    Callback for RadioButtons. 
    This updates the task list and forces a move to the next tab.
    We use root.after() to ensure the event loop processes this after the click.
    """
    # Get current list of tasks (in a real app, you'd update a state variable)
    try:
        with open(TASK_FILE, 'r') as f:
            current_tasks = json.load(f)
    except:
        return

    print(f"Status changed to: {status_type}")
    
    # Logic to simulate moving tab after delay (UI responsiveness)
    root.after(100, lambda: notebook.select(1))

# --- Build GUI ---
root = tk.Tk()
root.title("Tkinter Todo List - Notebook Demo")
root.geometry("500x400")

# Create Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# --- Tab 1: Progress (Input/Selection) ---
progress_frame = ttk.Frame(notebook)
notebook.add(progress_frame, text="Progress")

tk.Label(progress_frame, text="Select Task Status", font=("Arial", 14), pady=20).pack(pady=(0,10))

# We use Checkbuttons with variable logic or Radiobuttons if strictly exclusive.
# For this demo, we will simulate a single selection state per task using Radiobuttons for clarity.
tk.Label(progress_frame, text="Current Task Status:", font=("Arial", 12)).pack()

frame_rads = ttk.Frame(progress_frame)
frame_rads.pack()

# Variables to track current radio state (simulated)
var_status = tk.IntVar() # Simple int variable for demo selection

# Radio buttons acting as selectors for "Progress" stage
rad_pending = ttk.Radiobutton(
    frame_rads, 
    text="Pending", 
    variable=var_status, 
    value=0,
    command=lambda: handle_status_change("pending")
)
rad_pending.pack(side=tk.LEFT)

rad_progress = ttk.Radiobutton(
    frame_rads, 
    text="In Progress", 
    variable=var_status, 
    value=1,
    command=lambda: handle_status_change("in_progress")
)
rad_progress.pack(side=tk.LEFT)

rad_done = ttk.Radiobutton(
    frame_rads, 
    text="Finished", 
    variable=var_status, 
    value=2,
    command=lambda: handle_status_change("done")
)
rad_done.pack(side=tk.LEFT)

# Add a listbox to show current tasks (static for demo)
tk.Label(progress_frame, text="-- Tasks List --").pack()
lb_tasks = tk.Listbox(progress_frame, height=5)
for task in DEFAULT_TASKS:
    lb_tasks.insert(tk.END, f"{task['title']} ({task['status']})")
lb_tasks.pack(pady=10)

# --- Tab 2: Finish (Result/Summary) ---
finish_frame = ttk.Frame(notebook)
notebook.add(finish_frame, text="Finish")

tk.Label(finish_frame, text="Completed Tasks Summary", font=("Arial", 14), pady=20).pack()

# Entry to simulate typing a task before finishing
entry_task = tk.Entry(finish_frame, width=50)
entry_task.pack(pady=5)

btn_submit = ttk.Button(finish_frame, text="Add to Finished List", command=lambda: [
    messagebox.showinfo("Success", "Task moved to finish tab!"),
    notebook.select(0), # Optional: go back to progress or stay here
    entry_task.delete(0, tk.END)
])
btn_submit.pack(pady=10)

tk.Label(finish_frame, text="Result:", font=("Arial", 12)).pack()
text_result = tk.Text(finish_frame, height=8)
text_result.pack(pady=5)

# Initial Load Summary
for task in DEFAULT_TASKS:
    if task['status'] == 'done':
        text_result.insert(tk.END, f"✓ {task['title']}\n")

root.mainloop()