class Buku:
    def __init__(self, judul, penulis, isbn):
        self.judul = judul
        self.penulis = penulis
        self.isbn = isbn
        self.dipinjam = False

    def pinjam(self):
        if not self.dipinjam:
            self.dipinjam = True
            return True
        return False

    def kembalikan(self):
        if self.dipinjam:
            self.dipinjam = False
            return True
        return False

    def info(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"Judul: {self.judul}\nPenulis: {self.penulis}\nISBN: {self.isbn}\nStatus: {status}"

class AnggotaPerpustakaan:
    def __init__(self, nama, nomor_anggota):
        self.nama = nama
        self.nomor_anggota = nomor_anggota
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_dipinjam.append(buku)
            return True
        return False

    def kembalikan_buku(self, buku):
        if buku.kembalikan():
            self.buku_dipinjam.remove(buku)
            return True
        return False

    def daftar_buku_dipinjam(self):
        if not self.buku_dipinjam:
            return "Tidak ada buku yang dipinjam."
        daftar = "Buku yang dipinjam:\n"
        for buku in self.buku_dipinjam:
            daftar += f"- {buku.judul}\n"
        return daftar

# Contoh penggunaan
buku1 = Buku("Laskar Pelangi", "Andrea Hirata", "978-602-8699-01-3")
buku2 = Buku("Bumi", "Tere Liye", "978-602-062-212-7")

anggota1 = AnggotaPerpustakaan("Budi", "A001")

anggota1.pinjam_buku(buku1)
anggota1.pinjam_buku(buku2)

print(anggota1.daftar_buku_dipinjam())

anggota1.kembalikan_buku(buku1)

print(anggota1.daftar_buku_dipinjam())