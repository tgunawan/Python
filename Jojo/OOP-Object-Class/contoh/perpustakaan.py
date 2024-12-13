class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.tersedia = True


    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

    def kembalikan(self):
        if not self.tersedia:
            self.tersedia = True
            print(f"Buku '{self.judul}' berhasil dikembalikan.")
        else:
            print(f"Buku '{self.judul}' sudah tersedia.")

buku1 = Buku("Python for Dummies", "Mark Lutz", 2013)
buku2 = Buku("Clean Code", "Robert C. Martin", 2008)


buku1.pinjam()

buku2.kembalikan()   
