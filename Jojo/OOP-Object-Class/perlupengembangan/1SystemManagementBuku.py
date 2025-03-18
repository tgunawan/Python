class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def tampilkan_info(self):
        print(f"|{'Judul':<14}: {self.judul:<17}|")
        print(f"|{'Penulis':<14}: {self.penulis:<17}|")
        print(f"|{'Tahun Terbit':<14}: {self.tahun_terbit:<17}|")

class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_daftar_buku(self):
        if not self.daftar_buku:
            print("Perpustakaan kosong.")
        else:
            print("Daftar Buku:")
            for buku in self.daftar_buku:
                buku.tampilkan_info()
                print("-" * 20)

buku1 = Buku("Harry Potter", "J.K. Rowling", 1997)
buku2 = Buku("Lord of the Rings", "J.R.R. Tolkien", 1954)

perpustakaan = Perpustakaan()
perpustakaan.tambah_buku(buku1)
perpustakaan.tambah_buku(buku2)
perpustakaan.tampilkan_daftar_buku()


'''
tantangan:
-> Menambahkan tampilan system
-> Menambahkan fitur pencarian buku berdasarkan judul atau penulis.
-> Menambahkan fitur peminjaman dan pengembalian buku.
-> Menambahkan kelas AnggotaPerpustakaan untuk mengelola informasi anggota.
-> Menambahkan fitur penyimpanan data ke file
'''
