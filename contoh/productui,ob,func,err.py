import tkinter as tk
from tkinter import messagebox
import os

directory="./contoh/"
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (x{self.quantity})"

    def update_quantity(self, change):
        try:
            self.quantity += change
            if self.quantity < 0:
                raise ValueError("Quantity cannot be negative.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))  # Show error in a popup
            self.quantity -= change

    def to_txt_line(self):
        return f"{self.name},{self.price},{self.quantity}\n"

def load_products_from_txt(filename=directory+"products.txt"):
    products = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                    name, price, quantity = line.strip().split(',')
                    product = Product(name, float(price), int(quantity))
                    products.append(product)
                except ValueError as e:
                    print(f"Error loading product: {e}. Skipping this line.") # Print to console for debugging
    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found. Starting with an empty list.") # Print to console for debugging
    return products

def save_products_to_txt(products, filename=directory+"products.txt"):
    try:
        with open(filename, 'w') as f:
            for product in products:
                f.write(product.to_txt_line())
        print(f"Products saved to '{filename}' successfully.") # Print to console for debugging
        messagebox.showinfo("Success", f"Products saved to '{filename}' successfully.") # Show success message in popup
    except Exception as e:
        print(f"Error saving products to TXT: {e}") # Print to console for debugging
        messagebox.showerror("Error", f"Error saving products: {e}") # Show error in popup

def display_products(products, listbox):
    listbox.delete(0, tk.END)  # Clear the listbox
    for i, product in enumerate(products):
        listbox.insert(tk.END, f"{i+1}. {product}")

def add_product(products, name_entry, price_entry, quantity_entry, listbox):
    try:
        name = name_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        product = Product(name, price, quantity)
        products.append(product)
        display_products(products, listbox) # Update the displayed list
        name_entry.delete(0, tk.END) # Clear the entry fields
        price_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid price (number) and quantity (integer).")

def update_product_quantity(products, listbox):
    try:
        selected_index = listbox.curselection()
        if selected_index:
            index = selected_index[0]
            change = int(simpledialog.askstring("Update Quantity", "Enter quantity change:")) # Use simpledialog
            if change is not None: # Check if user cancelled the dialog
                products[index].update_quantity(change)
                display_products(products, listbox)
        else:
            messagebox.showwarning("Warning", "No product selected.")
    except (ValueError, IndexError):
        messagebox.showerror("Error", "Invalid input or no product selected.")

import tkinter.simpledialog as simpledialog # Import for quantity update dialog

# Main program
products = load_products_from_txt()

root = tk.Tk()
root.title("Product Management")

# Product Listbox
product_listbox = tk.Listbox(root, width=50)
product_listbox.pack(pady=10)
display_products(products, product_listbox)

# Input Frames
input_frame = tk.Frame(root)
input_frame.pack()

name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1)

price_label = tk.Label(input_frame, text="Price:")
price_label.grid(row=1, column=0)
price_entry = tk.Entry(input_frame)
price_entry.grid(row=1, column=1)

quantity_label = tk.Label(input_frame, text="Quantity:")
quantity_label.grid(row=2, column=0)
quantity_entry = tk.Entry(input_frame)
quantity_entry.grid(row=2, column=1)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Product", command=lambda: add_product(products, name_entry, price_entry, quantity_entry, product_listbox))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Quantity", command=lambda: update_product_quantity(products, product_listbox))
update_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(button_frame, text="Save Products", command=lambda: save_products_to_txt(products))
save_button.grid(row=0, column=2, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.grid(row=0, column=3, padx=5)

root.mainloop()