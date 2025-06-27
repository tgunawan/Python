import pandas as pd
import os 

def hapus():
    os.system('cls' if os.name == 'nt' else 'clear')

# hide simple indexed
'''print("Pandas version:", pd.__version__)
# jika tidak ada maka 
# pip install pandas

s=pd.Series([1, 2, 3, 4, 5])
print("Series s:\n", s)

s_indexed = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with custom index:\n", s_indexed)
s_dict = pd.Series({'b': 1, 'bc': 2, 'a': 3, 'd': 4, 'e': 5})
print("\nSeries from dictionary:\n", s_dict)
'''

# DF Data Frame
data={
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
hapus()
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

df.index = [1,2,3,4]  # Set custom index
print("\nDataFrame with custom index:\n", df)

df.info()
hapus()
df.describe()