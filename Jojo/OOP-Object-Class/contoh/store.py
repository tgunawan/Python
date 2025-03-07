class Produk:
    def __init__(self, nama, harga):
        self._nama = nama  # Atribut protected, bisa diakses langsung tapi tidak disarankan
        self.__harga = harga # Atribut private, sebaiknya hanya diakses melalui method

    def get_nama(self):
        return self._nama

    def set_nama(self, nama_baru):
        self._nama = nama_baru

    def get_harga(self):
        return self.__harga

    def set_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
        else:
            print("Harga tidak valid.")

    def info(self):
        return f"Nama: {self._nama}\nHarga: {self.__harga}"

class Toko:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def lihat_daftar_produk(self):
        if not self.daftar_produk:
            return "Tidak ada produk dalam daftar."
        daftar = f"Daftar Produk di {self.nama}:\n"
        for produk in self.daftar_produk:
            daftar += f"- {produk.info()}\n" 
        return daftar


produk1 = Produk("Sabun Mandi", 5000)
produk2 = Produk("Pasta Gigi", 7000)

toko_jaya = Toko("Toko Jaya")
toko_jaya.tambah_produk(produk1)
toko_jaya.tambah_produk(produk2)

print(toko_jaya.lihat_daftar_produk())

# Mengakses atribut protected (bisa, tapi tidak disarankan)
print(f"Nama produk 1 (langsung): {produk1._nama}")

# Mengakses atribut private (tidak disarankan, menggunakan name mangling)
#print(f"Harga produk 1 (langsung): {produk1._Produk__harga}") # Contoh name mangling, sebaiknya dihindari

# Menggunakan method untuk mengakses dan mengubah atribut private
print(f"Harga produk 1 (melalui method): {produk1.get_harga()}")
produk1.set_harga(5500)
print(f"Harga produk 1 (melalui method setelah diubah): {produk1.get_harga()}")

produk1.set_harga(-1000) 
print(f"Harga produk 1 (melalui method setelah diubah): {produk1.get_harga()}") #Harga tidak berubah