import tkinter as tk

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

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create the input field
equation = tk.StringVar()
expression_field = tk.Entry(window, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)

# Create buttons
button1 = tk.Button(window, text=' 1 ', command=lambda: button_click('1'), height=2, width=7)
button1.grid(row=2, column=0)
button2 = tk.Button(window, text=' 2 ', command=lambda: button_click('2'), height=2, width=7)
button2.grid(row=2, column=1)
button3 = tk.Button(window, text=' 3 ', command=lambda: button_click('3'), height=2, width=7)
button3.grid(row=2, column=2)
button4 = tk.Button(window, text=' 4 ', command=lambda: button_click('4'), height=2, width=7)
button4.grid(row=3, column=0)
button5 = tk.Button(window, text=' 5 ', command=lambda: button_click('5'), height=2, width=7)
button5.grid(row=3, column=1)
button6 = tk.Button(window, text=' 6 ', command=lambda: button_click('6'), height=2, width=7)
button6.grid(row=3, column=2)
button7 = tk.Button(window, text=' 7 ', command=lambda: button_click('7'), height=2, width=7)
button7.grid(row=4, column=0)
button8 = tk.Button(window, text=' 8 ', command=lambda: button_click('8'), height=2, width=7)
button8.grid(row=4, column=1)
button9 = tk.Button(window, text=' 9 ', command=lambda: button_click('9'), height=2, width=7)
button9.grid(row=4, column=2)
button0 = tk.Button(window, text=' 0 ', command=lambda: button_click('0'), height=2, width=15)
button0.grid(row=5, column=0, columnspan=2)

plus = tk.Button(window, text=' + ', command=lambda: button_click('+'), height=2, width=7)
plus.grid(row=2, column=3)
minus = tk.Button(window, text=' - ', command=lambda: button_click('-'), height=2, width=7)
minus.grid(row=3, column=3)
multiply = tk.Button(window, text=' * ', command=lambda: button_click('*'), height=2, width=7)
multiply.grid(row=4, column=3)
divide = tk.Button(window, text=' / ', command=lambda: button_click('/'), height=2, width=7)
divide.grid(row=5, column=3)

equal = tk.Button(window, text=' = ', command=equalto, height=2, width=7)
equal.grid(row=5, column=2)
clear = tk.Button(window, text='Clear', command=clear, height=2, width=7)
clear.grid(row=5, column=1)

window.mainloop()