'''
OOP Python = Class & Object
enkapsulasi=menyembunyikan detail object dari luar object
Abstraksi=menyederhanakan gambaran fitur dari object 
Inheritance=mewarisi properties / method dari parent class
Polimorfisme=memungkinkan object memanggil method dengan cara yang berbeda

'''
import os
os.system('cls')
'''Encapsulasi
class mobil: 
    def __init__(self, model, merek, tahun):
        self.model=model #encapsulasi data
        self.merek=merek#encapsulasi data=>Protected atau private
        self.tahun=tahun
        
    def info(self):
        return (f'Mobil ini adalah model {self.model},dengan merek mobil {self.merek} dan dari tahun{self.tahun}')

kendaraan1=mobil("Brio","Honda",2025)
print(kendaraan1.model)
print(kendaraan1.merek)
print(kendaraan1.info())


# Protected Private oop keamanan data
class AkunKeuangan:
    def __init__(self, nama, saldo):
        self._nama=nama #protected masih bisa di akses dari luar
        self.__saldo=saldo #private sudah tidak dapat di akses dari luar (keamanan)

    def masuk(self, jumlah):
        self.__saldo+=jumlah

    def keluar(self, jumlah):
        self.__saldo-=jumlah

    def displaySaldo(self):
        return self.__saldo
    
    def info(self):
        print(f'Nama Akun: {self._nama}')
        print(f'Saldo: {self.__saldo}')


myAccount=AkunKeuangan("Jojo", 100000)
myAccount.info()
myAccount.masuk(2000)
myAccount.__saldo="Script"
myAccount.info()
# print(myAccount.__saldo)
'''

'''# Abstraksi
# bentuk2D
# -persegi
# -segitiga
class bentuk2D: #kelas Abstract
    def luas(self):
        pass

class persegi(bentuk2D):
    def __init__(self,sisi):
        self.sisi=sisi

    def luas(self):
        return self.sisi*self.sisi
    
class segitiga(bentuk2D):
    def __init__(self,alas,tinggi):
        self.alas=alas
        self.tinggi=tinggi

    def luas(self):
        return (self.alas*self.tinggi)/2
    
segitiga1=segitiga(10,5)
persegi1=persegi(10)
print(segitiga1.luas())
print(persegi1.luas())'''

# Inheritance
# Simple Levelchild.py

# polimorfisme
class Burung:
    def suara(self):
        print("Cuitcuit")

class Anjing:
    def suara(self):
        print("Gongongong")

class Kucing:
    def suara(self):
        print("Meong")

def keluarkanSuara(hewan):
    hewan.suara()

burung=Burung()
anjing=Anjing()
kucing=Kucing()

keluarkanSuara(burung)
burung.suara()