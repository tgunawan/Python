import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Tkinter Project Template")
root.geometry("400x300")

# Function to handle button click
def on_button_click():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

# Create and place widgets
label = tk.Label(root, text="Enter something:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
root.mainloop()