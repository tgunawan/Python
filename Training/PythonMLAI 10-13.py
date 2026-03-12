'''Materi 10 Iris Dataset: Inspeksi Data & Visualisasi
Analisis dataset **Iris** adalah "Ritus Peralihan" (Rite of Passage) bagi setiap orang yang belajar Data Science. Dataset ini sangat bersih, seimbang, dan sempurna untuk memahami bagaimana fitur (karakteristik fisik) membedakan satu spesies dengan spesies lainnya.

---

## 1. Apa itu Dataset Iris?

Dataset ini berisi **150 data** bunga Iris yang terbagi ke dalam 3 spesies: **Setosa, Versicolor, dan Virginica**.

Setiap bunga diukur berdasarkan 4 fitur:

1. **Sepal Length** (Panjang Kelopak Luar)
2. **Sepal Width** (Lebar Kelopak Luar)
3. **Petal Length** (Panjang Mahkota)
4. **Petal Width** (Lebar Mahkota)

---

## 2. Data Inspection (Inspeksi Data)

Sebelum membuat model, kita harus "berkenalan" dulu dengan datanya. Kita perlu tahu:

* Apakah ada data yang kosong (Missing Values)?
* Bagaimana rentang angka pada setiap fitur?
* Apakah jumlah data antar spesies seimbang?

### Contoh Kode: Eksplorasi Dasar

```python
import pandas as pd
from sklearn.datasets import load_iris

# 1. Load data ke dalam format Pandas DataFrame agar mudah dibaca
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Mengubah angka (0,1,2) menjadi nama asli spesies agar mudah dipahami
df['species_name'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})

# 2. Inspeksi Awal
print("--- 5 Data Pertama ---")
print(df.head())

print("\n--- Info Struktur Data ---")
print(df.info())

print("\n--- Statistik Deskriptif ---")
print(df.describe())

print("\n--- Jumlah per Spesies ---")
print(df['species_name'].value_counts())

```

---

## 3. Visualisasi Distribusi Fitur

Angka di tabel seringkali membosankan dan sulit dibaca. Visualisasi membantu kita melihat "pemisahan" antar spesies secara instan.

### A. Histogram & KDE (Melihat Persebaran)

Kita ingin melihat fitur mana yang paling membedakan spesies. Biasanya, **Petal Length** adalah fitur yang paling "ajaib" karena memisahkan Setosa dengan sangat jelas dari spesies lainnya.

### B. Pairplot (Melihat Hubungan Antar Fitur)

Ini adalah teknik visualisasi paling ampuh di Iris. Ia membandingkan setiap fitur dengan fitur lainnya.

### Contoh Kode: Visualisasi

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set tema visualisasi
sns.set_theme(style="ticks")

# Visualisasi 1: Distribution Plot untuk Petal Length
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="petal length (cm)", hue="species_name", kde=True, element="step")
plt.title("Distribusi Panjang Mahkota (Petal) per Spesies")
plt.show()

# Visualisasi 2: Pairplot (Korelasi semua fitur)
# Kita bisa melihat fitur mana yang saling 'bertabrakan' dan mana yang terpisah jauh
sns.pairplot(df.drop('species', axis=1), hue="species_name", palette="bright")
plt.suptitle("Hubungan Antar Semua Fitur Iris", y=1.02)
plt.show()

```

---

## 4. Analisis Hasil Visualisasi

Setelah menjalankan kode di atas, kamu akan melihat beberapa pola menarik:

1. **Setosa adalah "Penyendiri":** Pada grafik, kelompok bunga Setosa biasanya terpisah sangat jauh dari dua spesies lainnya. Ini artinya Setosa sangat mudah dideteksi oleh AI.
2. **Versicolor vs Virginica:** Kedua spesies ini seringkali agak berhimpitan (*overlap*). Ini adalah bagian "sulit" di mana model ML harus bekerja lebih keras untuk membedakan keduanya.
3. **Petal vs Sepal:** Kamu akan melihat bahwa fitur **Petal** (mahkota) memberikan pemisahan yang lebih jelas dibandingkan fitur **Sepal**.

---

### Pentingnya Tahap Ini:

Banyak pemula langsung loncat ke `model.fit()`. Padahal, dengan melakukan inspeksi dan visualisasi, kita jadi tahu:

* Jika datanya berhimpitan, kita butuh model yang lebih kompleks (seperti Random Forest).
* Jika datanya terpisah jelas, model sederhana (seperti Linear SVC atau KNN) sudah cukup.

**Apakah kamu ingin mencoba teknik "Feature Engineering" (menggabungkan fitur untuk meningkatkan akurasi) atau langsung masuk ke tahap pembuatan model klasifikasi untuk dataset Iris ini?**
'''

'''kenapa pakai model ini
Penggunaan `RandomForestRegressor` dari library `scikit-learn` sangat populer untuk dataset seperti *California Housing* karena karakteristik datanya yang kompleks. Berikut adalah beberapa alasan teknis mengapa algoritma ini sering menjadi pilihan utama:

### 1. Menangani Hubungan Non-Linear

Data properti sering kali memiliki hubungan yang tidak sederhana (non-linear). Misalnya, harga rumah tidak selalu naik secara konstan seiring bertambahnya jumlah kamar; ada faktor lokasi (latitude/longitude) yang pengaruhnya sangat acak.

* **Linear Regression** mungkin gagal menangkap pola rumit ini.
* **Random Forest** menggunakan kumpulan "Decision Trees" yang bisa membagi data berdasarkan ambang batas tertentu, sehingga sangat fleksibel menangkap pola yang tidak beraturan.

### 2. Algoritma Ensemble (Kekuatan dalam Jumlah)

Sesuai namanya (`ensemble`), Random Forest bekerja dengan cara membuat banyak pohon keputusan (Decision Trees) secara acak, lalu mengambil rata-rata dari hasil prediksi semua pohon tersebut.

* Ini mencegah **Overfitting**: Jika hanya pakai satu pohon, model cenderung "menghafal" data latihan. Dengan banyak pohon, kesalahan dari satu pohon akan dikoreksi oleh pohon lainnya.

### 3. Ketahanan Terhadap Outliers

Dalam data perumahan, sering ada data "aneh" (outliers), seperti rumah yang sangat tua tapi harganya sangat mahal karena nilai sejarah. Random Forest cenderung lebih stabil dan tidak mudah terganggu oleh data ekstrem dibandingkan dengan model berbasis gradien atau garis lurus.

### 4. Skalabilitas dan Fitur Penting

* **Tanpa Scaling:** Berbeda dengan algoritma seperti SVM atau KNN, Random Forest tidak mewajibkan Anda untuk melakukan *feature scaling* (seperti merubah data ke skala 0-1). Ia bisa memproses angka ribuan (jumlah kamar) dan angka kecil (income) secara bersamaan tanpa masalah.
* **Feature Importance:** Setelah training, Anda bisa melihat fitur mana yang paling berpengaruh terhadap harga (misalnya, ternyata `median_income` jauh lebih penting daripada `total_rooms`).

---

### Ringkasan Perbandingan

| Fitur | Linear Regression | Random Forest |
| --- | --- | --- |
| **Pola Data** | Harus garis lurus | Bisa pola apa saja |
| **Akurasi** | Cenderung rendah pada data kompleks | Biasanya sangat tinggi |
| **Persiapan Data** | Butuh banyak normalisasi | Sangat minim persiapan |
| **Interpretasi** | Sangat mudah | Sedikit lebih kompleks |

---

**Apakah Anda ingin mencoba membandingkan akurasinya dengan model lain seperti `LinearRegression` untuk melihat perbedaannya secara langsung di Google Colab?**'''

'''Tes pemakaian model yang sudah dilatih dengan input dari user. Pastikan model sudah dilatih di cell sebelumnya agar variabel `model` tersedia untuk digunakan di sini.

Berikut adalah pembagian cell yang bisa Anda salin langsung ke Google Colab:

---

### Cell 1: Loading Data dan Pelatihan Model

Di sini kita memuat dataset bawaan Google Colab, menentukan target (harga rumah), dan melatih modelnya.

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# 1. Load Dataset
train_df = pd.read_csv('/content/sample_data/california_housing_train.csv')

# 2. Menentukan Fitur (X) dan Target (y)
# Kita gunakan fitur utama: longitude, latitude, housing_median_age, total_rooms, median_income
features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'median_income']
X = train_df[features]
y = train_df['median_house_value']

# 3. Inisialisasi dan Latih Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

print("Model berhasil dilatih!")

```

---

### Cell 2: Inferensi dengan Input User

Karena model sudah tersimpan di variabel `model` pada memori Colab, kita bisa langsung memanggilnya di cell baru.

```python
import numpy as np

print("--- Prediksi Harga Rumah California ---")

# Mengambil input dari user
try:
    lon = float(input("Masukkan Longitude (contoh: -114.3): "))
    lat = float(input("Masukkan Latitude (contoh: 34.2): "))
    age = float(input("Usia Rumah (Median Age): "))
    rooms = float(input("Total Kamar: "))
    income = float(input("Median Income (dalam puluhan ribu USD, contoh: 3.5): "))

    # Susun data input menjadi array 2D
    user_data = np.array([[lon, lat, age, rooms, income]])

    # Lakukan prediksi
    prediction = model.predict(user_data)

    print(f"\nPrediksi Harga Rumah: ${prediction[0]:,.2f}")

except ValueError:
    print("Mohon masukkan angka yang valid.")

```

---

### Penjelasan Singkat Alur Kerja:

* **Data Splitting:** Pada contoh di atas, kita menggunakan seluruh data `train` untuk melatih model agar akurasinya maksimal terhadap data yang tersedia di file tersebut.
* **Feature Selection:** Kita hanya mengambil beberapa kolom yang paling berpengaruh (seperti lokasi dan pendapatan) agar proses input user tidak terlalu panjang.
* **Persistent Variable:** Di Google Colab, selama *runtime* tidak di-restart, variabel `model` akan tetap hidup dan bisa diakses oleh cell mana pun di bawahnya.

**Apakah Anda ingin saya menambahkan metrik evaluasi (seperti MAE atau R-Squared) untuk melihat seberapa akurat model tersebut sebelum digunakan untuk prediksi?**
'''

'''Materi 11 - 13
Tentu, mari kita bedah konsep **Supervised Learning** ini secara mendalam agar Anda bisa menyampaikannya dengan struktur yang kuat untuk materi pembelajaran.

---

## 1. Perbedaan Mendasar: Klasifikasi vs Regresi

Inti dari Supervised Learning adalah melatih model dengan data yang sudah memiliki "jawaban" (label). Perbedaannya terletak pada **tipe jawaban** yang ingin diprediksi:

### **Classification (Klasifikasi)**

* **Output:** Kategori, Label, atau Kelas (Diskret).
* **Tujuan:** Memasukkan data ke dalam kotak-kotak tertentu.
* **Contoh:** Apakah siswa ini Lulus atau Tidak Lulus? Apakah email ini Spam atau Bukan?
* **Kapan Pakai?** Saat pertanyaan Anda dimulai dengan "Apakah..." atau "Termasuk golongan mana...".

### **Regression (Regresi)**

* **Output:** Angka kontinu (Numerik).
* **Tujuan:** Memprediksi nilai spesifik pada rentang angka tertentu.
* **Contoh:** Berapa nilai ujian siswa ini (0-100)? Berapa harga rumah ini?
* **Kapan Pakai?** Saat pertanyaan Anda dimulai dengan "Berapa banyak..." atau "Berapa nilai...".

---

## 2. Praktik di Google Colab: Classification

**(Materi 11 & 12)**

Kita akan menggunakan data **California Housing**, tapi kita ubah menjadi masalah klasifikasi: "Apakah rumah ini mahal (di atas rata-rata) atau tidak?"

### Cell 1: Persiapan Data & Preprocessing

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('/content/sample_data/california_housing_train.csv')

# Membuat Label Klasifikasi: 1 jika harga > median, 0 jika dibawah
median_price = df['median_house_value'].median()
df['is_expensive'] = (df['median_house_value'] > median_price).astype(int)

# Fitur dan Label
X = df[['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'median_income']]
y = df['is_expensive']

# Normalisasi (Penting untuk KNN)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

```

### Cell 2: Modeling (Decision Tree & KNN)

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

# 2. KNN
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)
knn_preds = knn_model.predict(X_test)

print("Akurasi Decision Tree:", accuracy_score(y_test, dt_preds))
print("Akurasi KNN:", accuracy_score(y_test, knn_preds))
print("\nConfusion Matrix (KNN):\n", confusion_matrix(y_test, knn_preds))

```

---

## 3. Praktik di Google Colab: Regression

**(Materi 13)**

Di sini kita memprediksi nilai asli `median_house_value`.

### Cell 3: Modeling (Linear Regression & Random Forest)

```python
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Gunakan data asli (y adalah harga, bukan kategori)
y_reg = df['median_house_value']
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# 1. Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train_r, y_train_r)
lr_preds = lr_model.predict(X_test_r)

# 2. Random Forest Regression
rf_model = RandomForestRegressor(n_estimators=50)
rf_model.fit(X_train_r, y_train_r)
rf_preds = rf_model.predict(X_test_r)

# Evaluasi
def evaluate(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"--- {name} ---")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2 Score: {r2:.2f}\n")

evaluate(y_test_r, lr_preds, "Linear Regression")
evaluate(y_test_r, rf_preds, "Random Forest Regressor")

```

---

## Ringkasan Evaluasi untuk Siswa

| Metode | Evaluasi Utama | Makna Sederhana |
| --- | --- | --- |
| **Klasifikasi** | **Accuracy** | Seberapa sering model menebak kategori dengan benar? |
|  | **Precision/Recall** | Seberapa baik model menangani kesalahan (salah tebak lulus/gagal)? |
| **Regresi** | **MAE (Mean Absolute Error)** | Rata-rata selisih angka prediksi dengan angka asli (misal: meleset $500). |
|  | **RMSE** | Memberikan bobot lebih besar pada kesalahan prediksi yang fatal/jauh. |

**Apakah Anda ingin saya membuatkan template kuis atau ringkasan materi dalam bentuk poin-poin untuk dibagikan kepada siswa?**
'''

'''pengunaan evaluasi
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder
import kagglehub

# Langkah 1: Unduh dataset dari Kaggle
path = kagglehub.dataset_download("ayeshasal89/ai-assistant-usage-in-student-life-synthetic")
print("Path to dataset files:", path)

# Memuat dataset
df = pd.read_csv(f"{path}/ai_assistant_usage_student_life.csv")

# Langkah 2: Pra-pemrosesan Data
# Menghilangkan kolom yang tidak relevan
df = df.drop(['SessionID', 'StudentLevel', 'SessionDate'], axis=1)

# Mengubah data kategorikal menjadi numerik
le = LabelEncoder()
for column in ['Discipline', 'TaskType', 'FinalOutcome']:
    if column in df.columns:
        df[column] = le.fit_transform(df[column])

# Menyiapkan fitur (X) dan target (y)
X = df.drop('UsedAgain', axis=1)
y = df['UsedAgain']

# Langkah 3: Pembagian Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ----- Penyempurnaan Kode: Hyperparameter Tuning dengan GridSearchCV -----
# Definisikan parameter yang akan diuji
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]}

# Inisialisasi model Random Forest
rf_model = RandomForestClassifier(random_state=42)

# Inisialisasi Grid Search
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Cetak parameter terbaik
print("\nParameter terbaik:", grid_search.best_params_)

# Gunakan model terbaik dari Grid Search untuk prediksi
best_model = grid_search.best_estimator_
y_pred_tuned = best_model.predict(X_test)

# Evaluasi model yang disempurnakan
print("\n--- Hasil Evaluasi Model Setelah Tuning ---")
print("Akurasi: ", accuracy_score(y_test, y_pred_tuned))
print("\nLaporan Klasifikasi:\n", classification_report(y_test, y_pred_tuned, zero_division=0))
'''

'''visualisasi hasil evaluasi
import matplotlib.pyplot as plt
import seaborn as sns

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
            xticklabels=['Tidak Digunakan Lagi', 'Digunakan Lagi'],
            yticklabels=['Tidak Digunakan Lagi', 'Digunakan Lagi'])
plt.title('Visualisasi Matriks Kebingungan')
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.show()

# Mengambil nilai feature importance dari model
feature_importance = model.feature_importances_
# Mengambil nama fitur
feature_names = X.columns
# Membuat DataFrame untuk memudahkan sorting
importance_df = pd.DataFrame({'feature': feature_names, 'importance': feature_importance})
# Mengurutkan fitur berdasarkan kepentingannya secara menurun
importance_df = importance_df.sort_values(by='importance', ascending=False)
plt.figure(figsize=(10, 7))
sns.barplot(x='importance', y='feature', data=importance_df, palette='viridis')
plt.title('Plot Kepentingan Fitur (Feature Importance Plot)')
plt.xlabel('Tingkat Kepentingan')
plt.ylabel('Fitur')
plt.tight_layout()
plt.show()
'''