import pandas as pd

Directory = "Jojo/NumpyPandas"
df = pd.read_csv(f"{Directory}/ContohData1.csv")
print(df)

# select berdasarkan kolom
#================================
# print("\nSelect berdasarkan kolom:",df['Name']) # 1 kolom
print("\nSelect berdasarkan kolom:\n",df[['Name','Matematika']]) # 2 kolom

# select berdasarkan baris
print("\nSelect berdasarkan baris:\n",df.iloc[0:3]) # 3 baris pertama dari index 0-2

#print tanpa index
print("\nSelect berdasarkan baris tanpa index:\n",df.iloc[0:3].to_string(index=False))

#print baris dan kolom tertentu
print("\nSelect baris dan kolom tertentu:\n",df.iloc[[0,3], [0,3]])
print("\nSelect baris dan kolom tertentu:\n",df.iloc[0:3, 0:2]) # 3 baris pertama dan 2 kolom pertama
print(df.loc[[0,3],['Name','Matematika']]) # 3 baris pertama dan 2 kolom pertama baris int, kolom string

#=================================

#Filtering data

# Filter berdasarkan kondisi
print("\nSelect berdasarkan kondisi:\n",df[df['Matematika'] > 80]) # Matematika > 80
print("\nSelect berdasarkan kondisi:\n",df[df["Name"] == "Alice" ])

# Filter berdasarkan beberapa kondisi or AND
print(df[(df['Matematika']<80)&(df['Science']<80)]) # Matematika dan Science < 80

#==================================

# Merging / Joining DataFrames
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df_orders = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'CustomerID': [1, 2, 2, 4, 5],
    'Product': ['Laptop', 'Tablet', 'Smartphone', 'Monitor', 'Keyboard'],
})

# Merge DataFrames
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='inner') # merge data yang full terisi dan skip yang kosong
print("\nHasil merge DataFrames:\n", df_merged)
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
print("\nHasil merge DataFrames Left:\n", df_merged)
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='right')
print("\nHasil merge DataFrames Right:\n", df_merged)
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
print("\nHasil merge DataFrames Outier:\n", df_merged)

