#---- Level 1 class----
class Hewan():
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Hewan bersuara")

#---- Level 2 class----
class Mamalia(Hewan):
    def menyusui(self):
        print("Mamalia menyusui")

class Unggas(Hewan):
    def bertelur(self):
        print("Unggas bertelur")

#---- Level 3 class----
class Anjing(Mamalia):
    def berbicara(self):
        print("Anjing menggonggong")
class Burung(Unggas):  
    def berbicara(self, suara="Cuitcuit"):
        print(self.nama, "Burung berkicau",suara)

anjingku = Anjing("Husky")
merpati = Burung("Merpati")

print(anjingku.nama)  # Hasil: Husky
anjingku.bersuara()  # Hasil: Hewan bersuara
anjingku.menyusui()  # Hasil: Mamalia menyusui
anjingku.berbicara()  # Hasil: Anjing menggonggong
merpati.berbicara()
merpati.berbicara("kakak kakak")