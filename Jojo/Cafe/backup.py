#------------library------------
import os
from datetime import datetime
import time
import fungsi as f

#------------variable------------
ListMenu = []
ListMinum = []
ListSnack = []
ListOrder = []
directory='./Jojo/Cafe'
#------------function------------
def clear():
    os.system('cls')
def GetData(menu,List):
    with open(f'{directory}/{menu}.txt', 'r') as file:
        for line in file:
            List.append(line.strip())

def MenuChoice():
    op2=int(input(f'Choice:\n1. Food\n2. Minum\n3. Snack\nMasukkan pilihan: '))
    if op2==1:
        displayList(ListMenu)
        return 1
    elif op2==2:
        displayList(ListMinum)
        return 2
    elif op2==3:
        displayList(ListSnack)
        return 3
    else:
        input("Input salah")
        MenuChoice()

def orderChoice(op2):
    order1=int(input("Masukkan nomor menu: "))
    if op2==1:
        ListOrder.append(ListMenu[order1-1])
    elif op2==2:
        ListOrder.append(ListMinum[order1-1])
    elif op2==3:
        ListOrder.append(ListSnack[order1-1])
    else:
        input("Input salah")
        orderChoice(op2)
    back=int(input("1. Pesan lagi\n2. Back to menu \n3. Back to main menu\nMasukkan pilihan: "))
    if back==1:
        orderChoice(op2)
    elif back==2:
        enddata()
        MenuChoice()
    elif back==3:
        enddata()
        clear()
def displayList(ListMenu):
    clear()
    for i in range(len(ListMenu)):
        print(ListMenu[i])

def enddata():
    with open(f'{directory}/orderData.txt', 'a') as file:
        for line in ListOrder:
            # print(line)
            file.write(datetime.now().strftime('%Y-%m-%d %H:%M') + '\n')
            file.write(line + '\n')


#------------main------------
GetData('food',ListMenu)
GetData('minum',ListMinum)
GetData('snack',ListSnack)

while True:
    clear()
    print(f'Selamat datang di cafe Jojo')
    op1=int(input(f'Choice:\n1. Lihat menu\n2. Keluar\nMasukkan pilihan: '))
    if op1==1:
        op2=MenuChoice()
        orderChoice(op2)
    elif op1==2:
        exit("Terimakasih telah berkunjung")
    else:
        input("Input salah")






#------------end------------


#example2D
# def GetData(directory):
#     with open(f'{directory}/dataCafe.txt', 'r') as file:
#         for line in file:
#             part=line.strip().split('|')
#             ListMenu.append(part)

# GetData(directory)
# print(ListMenu)
# for i in range(len(ListMenu)):
#     print(" ".join(ListMenu[i]))

# " | ".join(ListMenu[i])

# print(ListMenu)
# print(ListMinum)
# print(ListSnack)