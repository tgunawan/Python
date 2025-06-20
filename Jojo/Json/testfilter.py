import os, time, json

directory = "./Jojo/Json/"
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data_from_json(filename="sales_data.json", directory="./Jojo/Json/"):
    clear_screen()
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        print(f"Error: Data file not found at {filepath}. Please run data_generator.py first.")
        return None
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        print(f"Successfully loaded data from {filepath}")
        return data
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. File might be corrupted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading data: {e}")
        return None
    
def display_categories(data):
    clear_screen()
    if not data:
        print("\n--- No data to display ---")
        return

    categories = set(record["city"] for record in data)
    print("\n--- Available Categories ---")
    for category in sorted(categories):
        print(f"- {category}")
    
    print("\nPress Enter to continue...")
    input()

display_categories(load_data_from_json())