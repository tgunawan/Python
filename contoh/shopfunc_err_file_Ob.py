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
            print(f"Error: {e}")
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
                    print(f"Error loading product: {e}. Skipping this line.")
    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found. Starting with an empty list.")
    return products

def save_products_to_txt(products, filename=directory+"products.txt"):
    try:
        with open(filename, 'w') as f:
            for product in products:
                f.write(product.to_txt_line())
        print(f"Products saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Error saving products to TXT: {e}")

def display_products(products):
    if not products:
        print("No products in the list.")
        return
    print("Available Products:")
    for i, product in enumerate(products):
        print(f"{i+1}. {product}")

def add_product(products):
    try:
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        product = Product(name, price, quantity)
        products.append(product)
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid price (number) and quantity (integer).")

def update_product_quantity(products):
    display_products(products)
    try:
        index = int(input("Enter the index of the product to update: ")) - 1
        if 0 <= index < len(products):
            change = int(input("Enter the quantity change (positive to add, negative to subtract): "))
            products[index].update_quantity(change)
        else:
            print("Invalid product index.")
    except ValueError:
        print("Invalid input. Please enter a valid integer index and quantity change.")

# Main program
products = load_products_from_txt()

while True:
    print("\nProduct Management Menu:")
    print("1. Display Products")
    print("2. Add Product")
    print("3. Update Product Quantity")
    print("4. Save Products")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_products(products)
    elif choice == '2':
        add_product(products)
    elif choice == '3':
        update_product_quantity(products)
    elif choice == '4':
        save_products_to_txt(products)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting program.")