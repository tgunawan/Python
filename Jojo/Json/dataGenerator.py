import random
import json
import os

directory = "./Jojo/Json/"
def generate_sales_data(num_records=10):
    
    sales_records = []
    product_categories = ["Electronics", "Clothing", "Home Goods", "Books", "Food"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

    for i in range(num_records):
        record = {
            "transaction_id": f"TRX-{i+1:04d}", 
            "category": random.choice(product_categories),
            "amount": round(random.uniform(10.0, 500.0), 2), 
            "quantity": random.randint(1, 10),
            "city": random.choice(cities),
            "is_online_purchase": random.choice([True, False]),
            "rating": random.randint(1, 5)
        }
        sales_records.append(record)
    return sales_records

def save_data_to_json(data, filename="sales_data.json"):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}/")

    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\nGenerated data saved to {filepath}")

if __name__ == "__main__":
    num_records_to_generate = 20
    my_sales_data = generate_sales_data(num_records=num_records_to_generate)

    print("--- Generating Sales Data ---")
    print(f"Total records to generate: {len(my_sales_data)}")

    save_data_to_json(my_sales_data)

    print("\n--- First 3 Generated Records (for preview) ---")
    print(json.dumps(my_sales_data[:3], indent=2))