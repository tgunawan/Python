#--------library--------
import os


#--------class / function--------
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.tersedia = True

    def viewDetailed(self):
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Tersedia: {'Ya' if self.tersedia else 'Tidak'}")

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

def listbuke():
    for i in range(len(listBuku)):
        print(f'{i+1}. {listBuku[i]}')
    print('')

def clear():
    os.system('cls')
#--------object / variable--------
buku1 = Buku("Python for Dummies", "Mark Lutz", 2013)
buku2 = Buku("Clean Code", "Robert C. Martin", 2008)
listBuku=[]
pilihanbuku=''
#-------- main --------

clear()
listBuku.append(buku1.judul)
listBuku.append(buku2.judul)

while True:
    print(f'Selamat datang di perpustakaan Jojo')
    print(f'Choice:\n1. Lihat detail buku\n2. Pinjam buku\n3. Kembalikan buku\n4. Keluar')
    choice = int(input('Masukkan pilihan: '))
    listbuke()
    nobuku = int(input('Masukkan nomor buku: '))
    if nobuku == 1:
        pilihanbuku=buku1
    elif nobuku == 2:
        pilihanbuku=buku2

    if choice == 1:
        pilihanbuku.viewDetailed()
    elif choice == 2:
        pilihanbuku.pinjam()
    elif choice == 3:
        pilihanbuku.kembalikan()
    elif choice == 4:
        break