'''
# Data Netflix 2

1 load data
2. cleaning data (kosong, duplikat, transformasi, ubah tipe data)
3. Analisis Data
4. Sort, grouping, agregasi
5. Visualisasi Data (Matplotlib, Seaborn)'''

#---------- import library-----------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('Jojo/MachineLearningBeginner/KaggleVisualisasi/Netflix/netflix_titles.csv')
print(data.head()) #ambil 5 data teratas
print(data.info()) #menampilkan informasi data
print(data.describe()) #menampilkan statistik deskriptif
print(data.columns) #menampilkan nama kolom

#Cleaning data

data = data.dropna()# Hapus data kosong
data = data.drop_duplicates()# Hapus data duplikat  
data['release_year'] = data['release_year'].astype(int)# Ubah tipe data release_year jadi integer
data = data.dropna() #menghapus data yang kosong
data = data.drop_duplicates() #menghapus data yang duplikat
data['release_year'] = data['release_year'].astype(int) #mengubah tipe data release_year menjadi integer
#ambil data duration
#data['duration'] = data['duration'].str.replace(' min', '').astype(int) #mengubah tipe data duration menjadi integer
# Pisahkan durasi menjadi angka & tipe durasi
data['duration_num'] = data['duration'].str.extract('(\d+)').astype(int)
data['duration_type'] = data['duration'].apply(
    lambda x: 'min' if 'min' in str(x).lower() else 'season'
)

print(data.info()) #menampilkan informasi data

# ---------- 4. Analisis Data Sederhana ----------

print("\nJumlah konten per tipe:")
print(data['type'].value_counts())

print("\nTahun rilis terbanyak:")
print(data['release_year'].value_counts().head(5))

print("\nDurasi rata-rata film (menit):")
print(data[data['duration_type'] == 'min']['duration_num'].mean())

print("\nDurasi rata-rata TV Show (season):")
print(data[data['duration_type'] == 'season']['duration_num'].mean())

def typeasMovie():
    movie = data[data['type'].str.strip().str.lower() == 'movie']
    print(movie.head(10))

def typeasTVShow():
    tvshow = data[data['type'].str.strip().str.lower() == 'tv show']
    print(tvshow.head(10))

typeasMovie()  # Menampilkan 10 data teratas untuk tipe 'movie'
typeasTVShow()  # Menampilkan 10 data teratas untuk tipe 'tv show'

# ---------- 5. Sort, Grouping, Agregasi ----------

# Top 10 negara dengan konten terbanyak
top_country = data['country'].value_counts().head(10)

# Konten terbanyak per tahun
content_per_year = data.groupby('release_year')['show_id'].count().reset_index()
content_per_year = content_per_year.sort_values(by='show_id', ascending=False)

# ---------- 6. Visualisasi Data ----------

plt.figure(figsize=(8,5))
sns.countplot(data=data, x='type', palette='viridis')
plt.title('Jumlah Konten per Tipe')
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x=top_country.values, y=top_country.index, palette='coolwarm')
plt.title('Top 10 Negara dengan Konten Terbanyak')
plt.xlabel('Jumlah Konten')
plt.ylabel('Negara')
plt.show()

plt.figure(figsize=(12,6))
sns.lineplot(data=content_per_year, x='release_year', y='show_id', marker='o')
plt.title('Jumlah Konten per Tahun')
plt.xlabel('Tahun Rilis')
plt.ylabel('Jumlah Konten')
plt.show()