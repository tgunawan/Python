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
'''data={
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
# hapus()
print(df.describe())
# ProjectSalesData1.py #Pemakaian simple Pandas untuk analisis data penjualan
'''

#Sample dengan CSV file atau Comma separated values

csv_content = """
Name,Matematika,Science,English
Alice,90,85,88
Bob,75,40,35
Charlie,92,30,32
David,40,50,45
Eve,60,70,80
"""
'''Name;Matematika;Science;English
Alice;90;85;88
Bob;75;40;35
Charlie;92;30;32
David;40;45;50
Eve;60;75;80
'''

with open('Jojo/NumpyPandas/ContohData1.csv', 'w') as f:
    f.write(csv_content.strip())
with open('Jojo/NumpyPandas/ContohData1.csv', 'r') as f:
    tes=f.read()
    print(tes)

df = pd.read_csv('Jojo/NumpyPandas/ContohData1.csv')
print("\nDataFrame from CSV:\n", df)

df.to_csv('Jojo/NumpyPandas/ContohData2.csv', index=False)
print('done')

=====================

import pandas as pd
import os
Directorti = "BelajarMesin/Numpystuff/NumpyPanda"

csv_content = """
Name,Matematika,Science,English
Alice,90,85,88
Bob,75,40,35
Charlie,92,30,32
David,40,50,45
Eve,60,70,80
"""
csv_content2 ='''
Name;Matematika;Science;English
Alice;90;85;88
Bob;75;40;35
Charlie;92;30;32
David;40;45;50
Eve;60;75;80
'''
with open(f"{Directorti}/data.csv", "w") as file:
    file.write(csv_content.strip())


df = pd.read_csv(f"{Directorti}/data.csv")
print(df)

df2=pd.DataFrame(csv_content2)
df2.to_csv(f"{Directorti}/data2.csv")
print('done')import pandas as pd
import os
Directorti = "BelajarMesin/Numpystuff/NumpyPanda"

csv_content = """
Name,Matematika,Science,English
Alice,90,85,88
Bob,75,40,35
Charlie,92,30,32
David,40,50,45
Eve,60,70,80
"""
csv_content2 ='''
Name;Matematika;Science;English
Alice;90;85;88
Bob;75;40;35
Charlie;92;30;32
David;40;45;50
Eve;60;75;80
'''
with open(f"{Directorti}/data.csv", "w") as file:
    file.write(csv_content.strip())


df = pd.read_csv(f"{Directorti}/data.csv")
print(df)

df2=pd.DataFrame(csv_content2)
df2.to_csv(f"{Directorti}/data2.csv")
print('done')