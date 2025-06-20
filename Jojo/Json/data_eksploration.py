import json

def load_data_from_json(filename="sales_data.json", directory="./Jojo/Json/"):
    filepath = f"{directory}{filename}"
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: Data file not found at {filepath}. Please run data_generator.py first.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. File might be corrupted.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while loading data: {e}")
        return []

my_sales_data = load_data_from_json()
print("--- Basic Data Exploration ---")
print(f"Total number of sales records: {len(my_sales_data)}")

# 1. Hitung Category
category_counts = {}
for record in my_sales_data:
    category = record['category']
    category_counts[category] = category_counts.get(category, 0) + 1
print("\nSales by Category:")
for category, count in category_counts.items():
    print(f"- {category}: {count} sales")

# 2. Hitung Total Penjualan
total_amount = 0
for record in my_sales_data:
    total_amount += record['amount']
print(f"\nTotal Sales Amount: ${total_amount:.2f}")

# 3. Hitung Rata-rata Pembelian
average_amount = total_amount / len(my_sales_data) if my_sales_data else 0
print(f"Average Purchase Amount: ${average_amount:.2f}")

# 4. Filter untuk Pembelian Online
online_purchases = [
    record for record in my_sales_data if record['is_online_purchase']
]
print(f"\nNumber of Online Purchases: {len(online_purchases)}")
# print("Example online purchase:", online_purchases[0] if online_purchases else "N/A")

# 5. mencari nilai max / min
if my_sales_data:
    amounts = [record['amount'] for record in my_sales_data]
    highest_amount = max(amounts)
    lowest_amount = min(amounts)
    print(f"\nHighest Purchase Amount: ${highest_amount:.2f}")
    print(f"Lowest Purchase Amount: ${lowest_amount:.2f}")

    # Find the record for the highest purchase
    highest_purchase_record = next(
        (record for record in my_sales_data if record['amount'] == highest_amount),
        None
    )
    if highest_purchase_record:
        print(f"Details of highest purchase: {json.dumps(highest_purchase_record, indent=2)}")

# 6. Grouping by city and sum amounts
sales_by_city = {}
for record in my_sales_data:
    city = record['city']
    amount = record['amount']
    sales_by_city[city] = sales_by_city.get(city, 0.0) + amount
print("\nTotal Sales by City:")
for city, total_sales in sales_by_city.items():
    print(f"- {city}: ${total_sales:.2f}")