'''


hasil test no 1
datainput={1:0,0:0}
print(datainput)
while True:
    try:
        userin=int(input("Input: "))
        if userin not in datainput:
            print("Input tidak valid. Masukkan angka 0 dan 1.")
        if userin in datainput:
            datainput[userin]+=1
            if datainput[userin] % 2 == 1:
                print("Output: Putih")
            else:
                print("Output: Kuning")
    except ValueError:
        print("Input tidak valid. Masukkan angka 0 dan 1.")

#dengan list
datainput = [0, 0]
print(datainput)

while True:
    try:
        userin = int(input("Input: "))
        if userin not in [0, 1]:
            print("Input tidak valid. Masukkan angka 0 dan 1.")
            continue

        datainput[userin] += 1
        print(datainput)
        if datainput[userin] % 2 == 1:
            print("Output: Putih")
        else:
            print("Output: Kuning")

    except ValueError:
        print("Input tidak valid. Masukkan angka 0 dan 1.")
'''

'''hasil test no 2
jumlah=int(input("Input: "))
for i in range(1, jumlah+1):
    if i==1:print(" "*(jumlah+1)+"*")
    print("*"*i)
'''

'''hasil test no 3

def pola_angka(n):
    for i in range(1, n + 1):
        print(str(i) * i)

hasil=int(input("Input: "))
pola_angka(hasil)'''

'''hasil test no 4
def tabel_perkalian():
    for i in range(0, 11):
        baris = ""
        for j in range(0, 11):
            baris += f"{i*j:4}"
        print(baris)

print("Tabel Perkalian")
tabel_perkalian()'''

'''hasil test no 5

nama=input("Input: ")
for i in range(3):
    # print((nama + ' ') * 5)
    print(" ".join([nama]*5))'''

# nama = 'Kevin'
# for i in range(3):
#     print((nama + ' ') * 5)

n=int(input("MAsukkan jumlah baris: "))
for i in range(1,n+1,2):
    print(f"{'*'*i:^{n+5}}")

import random

def angka_acak():
    angka = random.randint(1, 100)
    return angka

def cek_angka(jawab,soal):
    if jawab == soal:
        print(f"{jawab} adalah angka yang tepat!")
    elif jawab < soal:
        print(f"{jawab} terlalu kecil, coba lagi.")
    elif jawab > soal:
        print(f"{jawab} terlalu besar, coba lagi.")
    else:
        print("Input tidak valid. Masukkan angka antara 1 dan 100.")