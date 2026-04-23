# ==========================================
# MINI PYTHON BAHASA INDONESIA
# ==========================================

# =========================
# INPUT & OUTPUT
# =========================
tulis = print
masukan = input

# =========================
# TIPE DATA
# =========================
angka = int
desimal = float
teks = str
boolean = bool
daftar = list
tuplekan = tuple
himpunan = set
kamus = dict
byteskan = bytes

# =========================
# NILAI KHUSUS
# =========================
Kosong = None
Benar = True
Salah = False

# =========================
# MATEMATIKA
# =========================
mutlak = abs
pangkat = pow
bulatkan = round
jumlah = sum
minimum = min
maksimum = max

# =========================
# ITERASI
# =========================
rentang = range
hitung = enumerate
gabung = zip
saring = filter
petakan = map
urutkan = sorted
balik = reversed

# =========================
# LOGIKA
# =========================
semua = all
ada = any

# =========================
# KONVERSI & REPRESENTASI
# =========================
karakter = chr
kode = ord
formatkan = format
representasi = repr

# =========================
# PEMERIKSAAN
# =========================
tipe = type
adalah_instance = isinstance
adalah_subkelas = issubclass
punya_atribut = hasattr
ambil_atribut = getattr
set_atribut = setattr
hapus_atribut = delattr
direktori = dir
identitas = id

# =========================
# EKSEKUSI DINAMIS
# =========================
evaluasi = eval
eksekusi = exec
kompilasi = compile
impor = __import__

# =========================
# FILE
# =========================
buka = open

# =========================
# EXCEPTION (KESALAHAN)
# =========================
Kesalahan = Exception
KesalahanNilai = ValueError
KesalahanTipe = TypeError
KesalahanNama = NameError
KesalahanIndex = IndexError
KesalahanKunci = KeyError
KesalahanFile = FileNotFoundError
KesalahanImport = ImportError
KesalahanPembagianNol = ZeroDivisionError

# =========================
# KELAS UMUM
# =========================
Objek = object

# =========================
# FUNGSI TAMBAHAN KHUSUS MINI PYTHON
# =========================

def panjang(data):
    return len(data)

def tambah(daftar_objek, nilai):
    daftar_objek.append(nilai)

def hapus(daftar_objek, nilai):
    daftar_objek.remove(nilai)

def keluar():
    exit()

def tunggu():
    input("Tekan ENTER untuk lanjut...")