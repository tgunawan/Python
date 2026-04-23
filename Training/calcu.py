# Simple calculator app with a GUI built using Tkinter. Easy to understand and use, with error handling for invalid inputs and division by 0.
# Concepts Used:
    #- Variables: Used to store the window object (root), widgets (num1entry, operatormenu), and the numbers input by the user.
    #- Functions: The calculate function is defined to perform the math.
    #- Conditionals: if, elif, and else to determine which operation to perform based on the user's choice.
    #- Looping (Mainloop): Using root.mainloop() which is an infinite loop to keep the win open.
    #- List/Data Structure: Using a list in values=["+", "-", "*", "/"]' inside the Combobox widget to hold the operation choices.
    #- Error Handling: Using try & except ValueError to catch non-numeric input, and if num2 == 0 to prevent division by 0.
# Instructions:
    #- Run the script using Python.
    #- Enter numbers in the first and second input boxes.
    #- Select an operation from the dropdown menu.
    #- Calculate

# CODE:
import tkinter as tk
from tkinter import ttk

def calculate(): #Math function
    # Variables to store data from the user input boxes
    num1text = num1entry.get()
    num2text = num2entry.get()
    operation = operatormenu.get()

    try: # If the user typed "hello" instead of "5", this will trigger an error!
        num1 = float(num1text) # Convert the text into decimal numbers (floats)
        num2 = float(num2text)
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0: # Prevent division by zero
                label_result.config(text="Error: Can't divide by zero!")
                return 
            result = num1 / num2
        else:
            label_result.config(text="Error: Please select an operation.")
            return
        label_result.config(text=f"Result: {result}") # Update the result label
    except ValueError:
        label_result.config(text="Error: Please enter numbers only!") #If the user types something that can't be converted to a number.

#GUI
root = tk.Tk()
root.title("Chen Calculator")
root.geometry("350x250") # Program window size
tabber = ttk.Notebook(root) # Tab for instructions and calculator
tabber.pack(pady=10)

# --------Calculator Tab---------
tab_calc = ttk.Frame(tabber)
tabber.add(tab_calc, text="Calculator")

tk.Label(tab_calc, text="Number 1:").grid(row=0, column=0, padx=10, pady=10) # Widget Label to show "Number 1" next to the first entry box.
num1entry = tk.Entry(tab_calc, width=15) # Widget Entry to get the first number from the user. Num1entry.get() to get the text that the user typed in. 
num1entry.grid(row=0, column=1)

tk.Label(tab_calc, text="Operation:").grid(row=1, column=0, padx=10, pady=5) # Widget Combobox to let the user choose the operation. Operatormenu.get() to find out which operation the user chose.
operatormenu = ttk.Combobox(tab_calc, values=["+", "-", "*", "/"], state="readonly", width=7) # state="readonly" means the user can't type their own operation.
operatormenu.set("+") # Set the default to addition
operatormenu.grid(row=1, column=1)

tk.Label(tab_calc, text="Number 2:").grid(row=2, column=0, padx=10, pady=10)
num2entry = tk.Entry(tab_calc, width=15)
num2entry.grid(row=2, column=1)

btn_calc = tk.Button(tab_calc, text="Calculate it!", command=calculate) # When the button is clicked, it will run the calculate() function at the top.
btn_calc.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(tab_calc, text="Result: ", font=("Times", 12, "bold")) # Label for showing the result of the calculation or any error messages. label's text will get updated in the calculate() function.
label_result.grid(row=4, column=0, columnspan=2)

# --------Instruction Tab---------
tab_help = ttk.Frame(tabber)
tabber.add(tab_help, text="How to Use")

instructions = (
    "Welcome to the Simple Calculator!\n\n"
    "1. Go to the 'Calculator' tab.\n"
    "2. Type a number in the first box.\n"
    "3. Choose +, -, *, or / from the dropdown.\n"
    "4. Type a number in the second box.\n"
    "5. Click 'Calculate!'\n\n"
    "Try typing a letter instead of a number\n"
    "to see the error handling in action!"
)
tk.Label(tab_help, text=instructions, justify="left").pack(padx=20, pady=20)

# MAIN LOOP
root.mainloop()