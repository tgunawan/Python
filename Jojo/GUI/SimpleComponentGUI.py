# contoh penggunaan Entry / get data from entry
'''import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Text Entry")

def greet():
    name = entry.get()
    print("Hello,", name)

label = ttk.Label(root, text="Enter your name:")
label.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()'''

# contoh penggunaan Label dan pack side
'''import tkinter as tk

def create_biodata_form(root):
    # Create labels and entries for name, age, and address
    name_label = tk.Label(root, text="Name:")
    name_label.pack(side=tk.LEFT)
    name_entry = tk.Entry(root)
    name_entry.pack(side=tk.LEFT)

    age_label = tk.Label(root, text="Age:")
    age_label.pack(side=tk.TOP)
    age_entry = tk.Entry(root)
    age_entry.pack(side=tk.TOP)

    address_label = tk.Label(root, text="Address:")
    address_label.pack(side=tk.RIGHT)
    address_entry = tk.Entry(root)
    address_entry.pack(side=tk.RIGHT)

# Create the main window
root = tk.Tk()
root.title("Biodata Form")

# Create the biodata form
create_biodata_form(root)

root.mainloop()
'''

# contoh penggunaan Label dan grid(lokasi) = positioning
'''import tkinter as tk

def create_biodata_form(root):
    # Create labels and entries for name, age, and address
    name_label = tk.Label(root, text="Name:")
    #name_label.grid(row=0, column=0,columnspan=2, rowspan=2)
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    age_label = tk.Label(root, text="Age:")
    age_label.grid(row=1, column=0)
    age_entry = tk.Entry(root)
    age_entry.grid(row=1, column=1)

    address_label = tk.Label(root, text="Address:")
    address_label.grid(row=2, column=0)
    address_entry = tk.Entry(root)
    address_entry.grid(row=2, column=1)

# Create the main window
root = tk.Tk()
root.title("Biodata Form")

# Create the biodata form
create_biodata_form(root)

root.mainloop()'''

# contoh penggunaan Button dengan lamda / anonymous function + get data from button
'''import tkinter as tk

def button_click(char):
    global expression
    expression += char
    equation.set(expression)

def equalto():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

expression = ""

window = tk.Tk()
window.title("Simple Calculator")

equation = tk.StringVar()

expression_field = tk.Entry(window, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

button1 = tk.Button(window, text=' 1 ', command=lambda: button_click('1'), height=2, width=7)
button1.grid(row=2, column=0)

# ... similar buttons for other digits and operators

window.mainloop()'''


'''import tkinter as tk

root = tk.Tk()

# Create a label
label = tk.Label(root, text="Hello, World!", font=("Arial", 20))
label2 = tk.Label(root, text="Hello, World!2", font=("Arial", 20))


# label.pack(side=tk.TOP, anchor=tk.NW)  # Top-left corner
# label.pack(side=tk.TOP, anchor=tk.NE)  # Top-right corner
# label.pack(side=tk.TOP, anchor=tk.SW)  # Bottom-left corner
label.pack(side=tk.LEFT, anchor=tk.E)  # Bottom-right corner
label2.pack(side=tk.LEFT, anchor=tk.E)  # Bottom-right corner
# label.pack(side=tk.TOP, anchor=tk.CENTER)  # Center

root.mainloop()'''

'''import tkinter as tk

root = tk.Tk()

# Create a main frame
main_frame = tk.Frame(root)
main_frame.pack()

# Create a frame for the first row of widgets
row1_frame = tk.Frame(main_frame)
row1_frame.pack()

# Create a label and an entry for the first row
label1 = tk.Label(row1_frame, text="Label 1:")
label1.pack(side=tk.LEFT)
entry1 = tk.Entry(row1_frame)
entry1.pack(side=tk.LEFT)

# Create a frame for the second row of widgets
row2_frame = tk.Frame(main_frame)
row2_frame.pack()

# Create a label and an entry for the second row
label2 = tk.Label(row2_frame, text="Label 2:")
label2.pack(side=tk.LEFT)
entry2 = tk.Entry(row2_frame)
entry2.pack(side=tk.LEFT)

root.mainloop()'''

