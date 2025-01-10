#---------Libarary----------
import os

#---------Variable----------
dictionary = {
    #key : value
}
list=[]
BiodataSiswa1={'Nama':'Jojo',
            'Umur':20,
            'Alamat':'Bandung'} 

kontak={'Jojo':6212345678,
        'Budi':6213231123,
        'Andi':6216768787}

kelas12={
    'siswa1':{
        'Nama':'Jojo',
        'Umur':17,
        'Alamat':'Bandung'
    },
    'siswa2':{
        'Nama':'Budi',
        'Umur':18,
        'Alamat':'Bandung'
    },
    'siswa3':{
        'Nama':'Andi',
        'Umur':19,
        'Alamat':'Bandung'
    }
}


#---------Function----------    

#---------Main----------
os.system('cls')

print('====**Biodata Siswa**====')
# print(f'1. {kelas12["siswa1"]["Nama"]}')
# print(f'2. {kelas12["siswa2"]["Nama"]}')
# print(f'3. {kelas12["siswa3"]["Nama"]}')



'''
nama=input('Masukkan Nama : ')
if nama in kontak:
    print(f'Nomor telepon {nama} adalah +{kontak[nama]}')
else:
    print('data tidak di temukan')


BiodataSiswa1['Umur']=40
BiodataSiswa1['Sekolah']='Penabur   1'  #Nambah Dictionary
del BiodataSiswa1['Sekolah']            #Hapus Dictionary
print(BiodataSiswa1)                    #Seluruh Dictionary
print(BiodataSiswa1['Nama'])            #Hanya Nama
print(BiodataSiswa1['Umur'])            #Hanya Umur
print(BiodataSiswa1.keys())             #Hanya Key
print(BiodataSiswa1.values())           #Hanya isi
list.append(BiodataSiswa1)
print(list)'''

#---------End----------