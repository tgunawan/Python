#---------Libarary----------
import os

#---------Variable----------
dictionary = {}
list=[]

#---------Function----------    

#---------Main----------
os.system('cls')
BiodataSiswa1={'Nama':'Jojo',
            'Umur':20,
            'Alamat':'Bandung'} 
BiodataSiswa1['Umur']=40
BiodataSiswa1['Sekolah']='Penabur   1'  #Nambah Dictionary
del BiodataSiswa1['Sekolah']            #Hapus Dictionary
print(BiodataSiswa1)                    #Seluruh Dictionary
print(BiodataSiswa1['Nama'])            #Hanya Nama
print(BiodataSiswa1['Umur'])            #Hanya Umur
print(BiodataSiswa1.keys())             #Hanya Key
print(BiodataSiswa1.values())           #Hanya isi
list.append(BiodataSiswa1)
print(list)
#---------End----------