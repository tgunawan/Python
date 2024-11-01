import os

while True:
    os.system('cls')
    number=int(input('Masukkan angka: '))

    for i in range(number):
        for j in range(i+1):
            print(f'{i+1}',end='')
        print()
    input()