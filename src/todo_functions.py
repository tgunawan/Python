def save_tasks(tasks, filename="tasks.txt"):
    """Saves all tasks to a file."""
    try:
        with open(filename, "w") as file:
            for task in tasks:
                status, description = task
                file.write(f"{status}|{description}\n")
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False

def load_tasks(filename="tasks.txt"):
    """Loads all tasks from a file."""
    try:
        tasks = []
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    status, description = line.strip().split("|")
                    tasks.append((status, description))
        return tasks
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty list.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def add_task(tasks, description):
    """Adds a new task to the list with 'Incomplete' status."""
    tasks.append(("Incomplete", description))
    return len(tasks)  # Return new index (0-based index is one less than length)

def remove_task(tasks, index):
    """Removes a task by its index from the list."""
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed: {removed}")
        return True
    return False

def mark_complete(task_index, tasks):
    """Marks a specific task as complete."""
    if 0 <= task_index < len(tasks):
        status, desc = tasks[task_index]
        if status == "Incomplete":
            tasks[task_index] = ("Complete", desc)
            return True
    return False

def move_to_finish_tab():
    """Simulates moving to the 'Finish' tab (e.g., updates focus or logs action)."""
    print("Moving to Finish tab...")
    # In a real app, you might use root.focus_force() after disabling all radio buttons