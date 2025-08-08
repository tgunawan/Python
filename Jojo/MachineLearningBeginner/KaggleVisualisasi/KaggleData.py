#https://www.kaggle.com/
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#baca data set
df= pd.read_csv('Jojo/MachineLearningBeginner/KaggleVisualisasi/Breast_cancer_dataset.csv')

#ambil kolom angka
# numColumn= df.select_dtypes(include=[np.number]).columns #Tuple
# numColumn= df.select_dtypes(include=[np.number]).columns.tolist() #List
# dataArray = df[numColumn].to_numpy()
# print(dataArray)

''' #di hide
mean_vals = np.mean(dataArray, axis=0)  # Rata-rata tiap kolom
max_vals = np.max(dataArray, axis=0)    # Nilai maksimum tiap kolom
min_vals = np.min(dataArray, axis=0)    # Nilai minimum tiap kolom

print("Rata-rata:", mean_vals)
print("Nilai Maksimum:", max_vals)
print("Nilai Minimum:", min_vals)

print(dataArray[:5, :3]) # Menampilkan 5 baris pertama dan 3 kolom pertama
'''
#---------------------------------------------------------------------------
print(df.info()) #informasi jumlah dan nama kolom beserta tipe data
print(df.head()) # menampilkan 5 baris pertama

print(df.describe()) # otomatis menampilkan statistik deskriptif dari kolom numerik

print(df.isnull().sum()) # Mengecek jumlah nilai yang hilang (NaN) di setiap kolom
df=df.drop(columns=['Unnamed: 32']) # menghapus kolom Unnamed: 32 yang tidak diperlukan

numColumn= df.select_dtypes(include=[np.number]).columns.tolist() #List
dataArray = df[numColumn].to_numpy()

#fill missing value dengan rata-rata
df[numColumn]= df[numColumn].fillna(df[numColumn].mean())

df= df.drop_duplicates() # menghapus baris duplikat

# Transformasi kolom diagnosis (B=0, M=1)
df['diagnosis_num'] = df['diagnosis'].map({'B': 0, 'M': 1})
print(df[['diagnosis', 'diagnosis_num']].head())

