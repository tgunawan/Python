class buku:
    def __init__(self, judul):
        self.judul = judul
    def pinjem(self):
        print(f'pinjem buku {self.judul}')
    def kembali(self):
        print(f'mengembalikan buku {self.judul}')


buku1 = buku('tedcode101')
buku1.pinjem()