import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

# random=random.randint(1, 1000)# import random terlebih dahulu jika ingin menggunakan random

Directory = "Jojo/MachineLearningBeginner"
plt.style.use('seaborn-v0_8-darkgrid')

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
try:
    df = pd.read_csv(f"{Directory}/DataDummy.csv" , sep=';')
    print("Nama-nama kolom yang ada:")
    print(df.columns)
except FileNotFoundError:
    print("Error: File 'DataDummy.csv' tidak ditemukan. Pastikan file berada di direktori yang sama.")
    messagebox.showerror("Error", "File 'DataDummy.csv' tidak ditemukan.")
    exit()

# 3. Analisis Data Awal
print("--- Data Penjualan Komponen Komputer ---")
print("\nDataFrame:")
print(df)

print("\nInformasi DataFrame:")
df.info()

print("\nStatistik Deskriptif:")
print(df.describe())


df_plot = df.set_index('Bulan')
total_penjualan_produk = df_plot.sum()


def show_line_chart():
    """Menampilkan plot tren penjualan bulanan."""
    fig, ax = plt.subplots(figsize=(10, 6),num="Tren Penjualan Bulanan")
    df_plot.plot(kind='line', ax=ax, marker='o')
    ax.set_title('Tren Penjualan Produk per Bulan', fontsize=16)
    ax.set_xlabel('Bulan', fontsize=12)
    ax.set_ylabel('Jumlah Penjualan', fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(title='Produk')
    plt.tight_layout()
    plt.show()

def show_bar_chart():
    """Menampilkan diagram batang total penjualan per produk."""
    fig, ax = plt.subplots(figsize=(10, 6))
    total_penjualan_produk.plot(kind='bar', ax=ax, color=['skyblue', 'salmon', 'lightgreen', 'orange'])
    ax.set_title('Total Penjualan per Produk (Selama 12 Bulan)', fontsize=16)
    ax.set_xlabel('Produk', fontsize=12)
    ax.set_ylabel('Total Penjualan', fontsize=12)
    ax.tick_params(axis='x', rotation=0)
    plt.tight_layout()
    plt.show()

print("\n--- Hasil Analisis ---")
produk_terlaris = total_penjualan_produk.idxmax()
jumlah_terlaris = total_penjualan_produk.max()
print(f"Produk dengan penjualan tertinggi adalah '{produk_terlaris}' dengan total penjualan: {jumlah_terlaris}")

df['Total_Penjualan_Bulanan'] = df[['VGA', 'CPU', 'RAM', 'Laptop']].sum(axis=1)
bulan_terlaris = df.loc[df['Total_Penjualan_Bulanan'].idxmax()]['Bulan']
total_penjualan_bulan_terlaris = df['Total_Penjualan_Bulanan'].max()
print(f"Bulan dengan total penjualan paling tinggi adalah '{bulan_terlaris}' dengan total: {total_penjualan_bulan_terlaris}")

root = tk.Tk()
root.title("Aplikasi Visualisasi Penjualan")
root.geometry("400x200") 

frame = ttk.Frame(root, padding="20")
frame.pack(expand=True, fill='both')

label_title = ttk.Label(frame, text="Pilih Visualisasi yang Ingin Ditampilkan:", font=("Helvetica", 14, "bold"))
label_title.pack(pady=10)

button_line = ttk.Button(frame, text="Tampilkan Tren Penjualan", command=show_line_chart)
button_line.pack(pady=5, ipadx=10, ipady=5)

button_bar = ttk.Button(frame, text="Tampilkan Total Penjualan", command=show_bar_chart)
button_bar.pack(pady=5, ipadx=10, ipady=5)

root.mainloop()