import json
import os

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

def display_records(records, title="All Records"):
    clear_screen()
    if not records:
        print(f"\n--- No {title} to display ---")
        return

    print(f"\n--- {title} ({len(records)} records) ---")
    for i, record in enumerate(records):
        print(f"Record {i+1}:")
        for key, value in record.items():
            print(f"  {key}: {value}")
        print("-" * 20)

def filter_data(data):
    clear_screen()
    if not data:
        print("No data loaded to filter.")
        return []

    filtered_records = data
    print("\n--- Filter Options ---")
    print("1. Filter by Category")
    print("2. Filter by City")
    print("3. Filter by Online Purchase (True/False)")
    print("4. Filter by Minimum Amount")
    print("5. Filter by Minimum Rating")
    print("6. No filter (show all data)")
    print("7. Exit Filter Menu")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        category = input("Enter category (e.g., Electronics, Clothing): ").strip().title()
        filtered_records = [record for record in filtered_records if record["category"] == category]
        print(f"Filtering by Category: '{category}'")
    elif choice == '2':
        city = input("Enter city (e.g., New York, Los Angeles): ").strip().title()
        filtered_records = [record for record in filtered_records if record["city"] == city]
        print(f"Filtering by City: '{city}'")
    elif choice == '3':
        is_online = input("Is it an online purchase? (True/False): ").strip().lower()
        if is_online == "true":
            filtered_records = [record for record in filtered_records if record["is_online_purchase"]]
            print("Filtering by Online Purchase: True")
        elif is_online == "false":
            filtered_records = [record for record in filtered_records if not record["is_online_purchase"]]
            print("Filtering by Online Purchase: False")
        else:
            print("Invalid input for online purchase. Showing all records for this filter.")
    elif choice == '4':
        try:
            min_amount = float(input("Enter minimum amount: "))
            filtered_records = [record for record in filtered_records if record["amount"] >= min_amount]
            print(f"Filtering by Minimum Amount: ${min_amount:.2f}")
        except ValueError:
            print("Invalid amount. Showing all records for this filter.")
    elif choice == '5':
        try:
            min_rating = int(input("Enter minimum rating (1-5): "))
            if 1 <= min_rating <= 5:
                filtered_records = [record for record in filtered_records if record["rating"] >= min_rating]
                print(f"Filtering by Minimum Rating: {min_rating} stars")
            else:
                print("Rating must be between 1 and 5. Showing all records for this filter.")
        except ValueError:
            print("Invalid rating. Showing all records for this filter.")
    elif choice == '6':
        print("No filter applied.")
        return data 
    elif choice == '7':
        print("Exiting filter menu.")
        return None 
    else:
        print("Invalid choice. Showing all records for this filter.")
        return data 

    return filtered_records

def main():
    sales_data = load_data_from_json()

    if not sales_data:
        return

    while True:
        print("\n--- Main Menu ---")
        print("1. Display All Sales Data")
        print("2. Filter Sales Data")
        print("3. Exit")

        menu_choice = input("Enter your choice (1-3): ")

        if menu_choice == '1':
            display_records(sales_data, "All Sales Records")
        elif menu_choice == '2':
            filtered_results = filter_data(sales_data)
            if filtered_results is None: 
                continue
            display_records(filtered_results, "Filtered Sales Records")
        elif menu_choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()