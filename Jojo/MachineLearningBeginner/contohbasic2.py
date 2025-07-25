import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("--- Project: Simple Sales Data Analysis ---")
# 1. Raw Sales Data
# Each row represents a sales transaction: [ProductID, Quantity, UnitPrice]
sales_data_np = np.array([
    [101, 5, 12.50],  # Product 101, 5 units, $12.50/unit
    [102, 2, 25.00],  # Product 102, 2 units, $25.00/unit
    [101, 3, 12.50],
    [103, 1, 50.00],
    [102, 4, 25.00],
    [101, 8, 12.50],
    [104, 2, 8.00],
    [103, 2, 50.00],
    [101, 1, 12.50],
])

print("\n1. Raw Sales Data (NumPy Array):")
print(sales_data_np)
print("Shape:", sales_data_np.shape)

# Convert NumPy array to Pandas DataFrame for easier analysis
df_sales = pd.DataFrame(sales_data_np, columns=['ProductID', 'QuantitySold', 'PricePerUnit'])

print("\nSales Data (Pandas DataFrame):")
print(df_sales)
print("\nDataFrame Info:")
df_sales.info()

# --- 2. Data Cleaning/Preparation (Basic) ---

# Ensure numeric columns are treated as numeric
df_sales['ProductID'] = df_sales['ProductID'].astype(int)
df_sales['QuantitySold'] = df_sales['QuantitySold'].astype(int)
df_sales['PricePerUnit'] = df_sales['PricePerUnit'].astype(float)

# --- 3. Feature Engineering: Calculate Total Sale Amount ---
# Using element-wise multiplication
df_sales['TotalSaleAmount'] = df_sales['QuantitySold'] * df_sales['PricePerUnit']

print("\nSales Data with 'TotalSaleAmount':")
print(df_sales)

# --- 4. Data Aggregation and Analysis ---
print("\n--- Sales Analysis Results ---")

# a. Calculate Total Revenue
total_revenue = df_sales['TotalSaleAmount'].sum()
print(f"Total Revenue Generated: ${total_revenue:.2f}")

# b. Calculate Average Sale Amount
average_sale_amount = df_sales['TotalSaleAmount'].mean()
print(f"Average Sale Amount per transaction: ${average_sale_amount:.2f}")

# c. Find Top-Selling Products (by Quantity Sold and by Revenue)

# Group by ProductID and sum quantities
product_quantity_sold = df_sales.groupby('ProductID')['QuantitySold'].sum().sort_values(ascending=False)
print("\nTotal Quantity Sold per Product:")
print(product_quantity_sold)

# Group by ProductID and sum total sale amount
product_revenue = df_sales.groupby('ProductID')['TotalSaleAmount'].sum().sort_values(ascending=False)
print("\nTotal Revenue per Product:")
print(product_revenue)

print(f"\nTop Selling Product by Quantity: Product ID {product_quantity_sold.index[0]} ({product_quantity_sold.iloc[0]} units)")
print(f"Top Earning Product by Revenue: Product ID {product_revenue.index[0]} (${product_revenue.iloc[0]:.2f})")

# d. Distribution of sales (e.g., how many unique products)
num_unique_products = df_sales['ProductID'].nunique()
print(f"\nNumber of Unique Products Sold: {num_unique_products}")

# --- 5. Simple Conditional Selection/Filtering ---

# Find all sales transactions for a specific product (e.g., ProductID 101)
product_101_sales = df_sales[df_sales['ProductID'] == 101]
print("\nSales Transactions for Product ID 101:")
print(product_101_sales)

# Find transactions with a total sale amount greater than $50
high_value_sales = df_sales[df_sales['TotalSaleAmount'] > 50]
print("\nHigh-Value Sales Transactions (TotalSaleAmount > $50):")
print(high_value_sales)


# --- 6. Data Visualization with Matplotlib ---
print("\n--- Sales Data Visualizations ---")

# Set a style for better aesthetics (Matplotlib's default is good, but you can explore 'ggplot', 'seaborn-v0_8', etc.)
plt.style.use('default') # Or 'ggplot', 'seaborn-v0_8' if you have it etc.

# Visualization 1: Total Revenue per Product
plt.figure(figsize=(10, 6))
# Using plt.bar for more direct control
plt.bar(product_revenue.index.astype(str), product_revenue.values, color='skyblue')
plt.title('Total Revenue Generated per Product ID')
plt.xlabel('Product ID')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a grid for readability
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()

# Visualization 2: Total Quantity Sold per Product
plt.figure(figsize=(10, 6))
plt.bar(product_quantity_sold.index.astype(str), product_quantity_sold.values, color='lightcoral')
plt.title('Total Quantity Sold per Product ID')
plt.xlabel('Product ID')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Visualization 3: Distribution of Total Sale Amount (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(df_sales['TotalSaleAmount'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Distribution of Total Sale Amount per Transaction')
plt.xlabel('Total Sale Amount ($)')
plt.ylabel('Number of Transactions')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print("\n--- Analysis and Visualization Complete ---")