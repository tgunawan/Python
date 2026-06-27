class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def info(self):
        print(f"Nama Hero: {self.name}")
        print(f"Health: {self.health}")
        print(f"Power: {self.power}")

    def attack(self):
        print(f"{self.name} menyerang dengan kekuatan {self.power}!")


class Swordmaster(Hero):
    def __init__(self, name, health, power, style):
        super().__init__(name, health, power)
        self.style = style

    def info(self):
        print(f"Nama Hero: {self.name}")
        print(f"Health: {self.health}")
        print(f"Power: {self.power}")
        print(f"Gaya Pedang: {self.style}")

    def attack(self):
        print(f"{self.name} mengayunkan pedang {self.style} dengan damage {self.power}!")

    def dash(self):
        print(f"{self.name} melakukan serangan cepat dan bergerak seperti kilat!")


if __name__ == "__main__":
    hero = Hero("Knight", 100, 20)
    print("=== Hero Biasa ===")
    hero.info()
    hero.attack()

    print("\n=== Swordmaster ===")
    swordmaster = Swordmaster("Arin", 140, 35, "Iaido")
    swordmaster.info()
    swordmaster.attack()
    swordmaster.dash()


# Penjelasan panjang tentang OOP dan Inheritance:
# Program ini menunjukkan konsep Object-Oriented Programming (OOP) dalam Python.
# OOP adalah cara menulis program dengan memodelkan dunia nyata menjadi objek.
# Dalam OOP, kita membuat kelas sebagai blueprint atau cetak biru, lalu membuat objek dari kelas tersebut.
# Kelas Hero berfungsi sebagai kelas utama yang menjelaskan karakter dasar hero, seperti nama, health, dan power.
# Di dalam kelas Hero terdapat method __init__ untuk menginisialisasi data awal objek.
# Method info() digunakan untuk menampilkan informasi hero, sedangkan method attack() digunakan untuk melakukan serangan.
# Ketika kita membuat objek hero = Hero("Knight", 100, 20), maka objek tersebut memiliki atribut dan kemampuan yang sudah didefinisikan di kelas Hero.
# Konsep inheritance atau pewarisan muncul ketika kelas Swordmaster(Hero) dibuat.
# Artinya, kelas Swordmaster mewarisi semua atribut dan method dari kelas Hero.
# Dengan inheritance, kita tidak perlu menulis ulang kode yang sudah ada di kelas Hero.
# Kelas Swordmaster hanya menambahkan ciri khusus, yaitu gaya pedang, melalui atribut self.style.
# Kelas Swordmaster juga meng-override method info() dan attack() agar perilakunya lebih spesifik untuk swordmaster.
# Override artinya menulis ulang method yang sudah ada di class induk dengan perilaku yang berbeda.
# Selain itu, kelas Swordmaster menambahkan method baru yaitu dash() yang hanya ada di kelas turunan.
# Kata kunci super() digunakan untuk memanggil konstruktor kelas induk, sehingga data nama, health, dan power tetap diwariskan.
# Dengan begitu, kode menjadi lebih rapi, terstruktur, dan mudah dikembangkan.
# Contoh ini sangat cocok untuk mempelajari dasar OOP karena menunjukkan:
# 1. Class sebagai template
# 2. Object sebagai hasil dari class
# 3. Attribute sebagai data
# 4. Method sebagai perilaku
# 5. Inheritance sebagai pewarisan sifat
# 6. Polymorphism (dalam bentuk override) sebagai kemampuan method yang berbeda di kelas anak
# Jika ingin dikembangkan lebih lanjut, kalian bisa menambahkan kelas lain seperti Mage, Archer, atau Tank yang juga mewarisi Hero.
# Dengan pola ini, program menjadi lebih mudah dipelihara karena perubahan pada class induk bisa memengaruhi semua turunan secara konsisten.
# Inti dari OOP adalah mengorganisir kode berdasarkan objek dan fungsinya, bukan sekadar baris perintah yang berjalan berurutan.
