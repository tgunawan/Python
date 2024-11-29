class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan bersuara")

class Mamalia(Hewan):
    def menyusui(self):
        print("Mamalia menyusui")

class Anjing(Mamalia):
    def menggonggong(self):
        print("Anjing menggonggong")


anjingku = Anjing("Husky")

print(anjingku.nama)  # Hasil: Husky
anjingku.bersuara()  # Hasil: Hewan bersuara
anjingku.menyusui()  # Hasil: Mamalia menyusui
anjingku.menggonggong()  # Hasil: Anjing menggonggong