import os

os.system('clear')

#Komentar tidak terbaca di program
# Variable dasar = Char, String
# Penamaan Variable tidak boleh pakai angka/symbol di depan dan ada spasi
# print(f"nama saya {'Tedi':20}") contoh pemakaian kutip
os.system('clear')
nama="Katy"
usia=15
sekolah="SMAK 1 Penabur"
alamat='Jakarta Barat'

print("Hallo")
print('Nama saya: ',nama)
print('Usia saya: ',usia)
print('Saya sekolah di',sekolah)
print('Alamat saya di',alamat)
input()
os.system('clear')
nama=input('Masukkan nama: ')
usia=int(input('Masukkan usia kamu: '))
sekolah=input('Masukkan sekolah kamu: ')
alamat=input('Kamu tinggal dimana: ')
input('Press to continue...')

print("Hallo")
print('Nama saya: ',nama)
print('Usia saya: ',usia)
print('Saya sekolah di',sekolah)
print('Alamat saya di',alamat)

#second file
# #Chat Dummy
#pr Selamat datang di aplikasi Chat 
#in Silahkan masukkan nama kamu: "Nama"
#pr Selamat datang, "Nama"
#in Hari ini bagaimana kabarnya: "Kabar"
#pr Ohh, Ternyata hari ini kamu sedang, "Kabar"
#in Kamu usianya berapa: "12"
#pr oh kamu ternyata berusia "12"*2
#contoh ide boleh beda  makanan, minuman,usia,


print('Selamat datang di aplikasi Chat')
nama=input('Silahkan masukkan nama kamu: ')
print('Selamat datang',nama)
usia=int(input('Usia kamu '))
print('Usia saya',usia*2)