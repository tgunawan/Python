import json

directory="./contoh/"
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):  # For easy printing
        return f"{self.name} - ${self.price:.2f} (x{self.quantity})"

    def update_quantity(self, change):
        try:
            self.quantity += change
            if self.quantity < 0:
                raise ValueError("Quantity cannot be negative.")  # Custom error
        except ValueError as e:
            print(f"Error: {e}")
            self.quantity -= change # Revert the change if error occurs

    def to_dict(self): # For JSON serialization
        return {"name": self.name, "price": self.price, "quantity": self.quantity}


def load_products_from_json(filename=directory+"products.json"):
    try:
        with open(filename, 'r') as f:
            product_data = json.load(f)
            products = []
            for item in product_data:
                try: # Inner try-except for individual product errors
                    product = Product(item["name"], item["price"], item["quantity"])
                    products.append(product)
                except (KeyError, TypeError) as e:
                    print(f"Error loading product from JSON: {e}. Skipping this product.")
            return products
    except FileNotFoundError:
        print(f"Warning: File '{filename}' not found.  Starting with an empty product list.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'. Starting with an empty product list.")
        return []

def save_products_to_json(products, filename=directory+"products.json"):
    try:
        with open(filename, 'w') as f:
            product_list = [product.to_dict() for product in products] # Convert objects to dicts
            json.dump(product_list, f, indent=4) # Use indent for pretty printing
        print(f"Products saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Error saving products to JSON: {e}")


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
products = load_products_from_json()

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
        save_products_to_json(products)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")

print("Exiting program.")