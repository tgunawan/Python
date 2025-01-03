import os,time,random
from datetime import datetime
directorti='./HandsomeCafe'

def Print(something):
    print(something)
def startData(menu,Varieble):
    with open(f'{directorti}/{menu}.txt','r') as file:
        for line in file:
            part=line.strip().split('|')
            Varieble.append(part)
            #print(part)
def displayList(Varieble):
    for i in range(len(Varieble)):
        print(f'{i+1:>5}.',end='')
        for j in range(len(Varieble[i])):
            print(f'{Varieble[i][j]:^17}',end='')
        print()
def opChoice(Food,Drinks,Snack,Order):
    os.system('cls')
    print('='*39)
    n=input('1.Food\n2.Drinks\n3.Snack\nWhat would you like to order? ')
    idk(n,Food,Drinks,Snack,Order)
def asnChoice(n,Food,Drinks,Snack):
    os.system('cls')
    print('='*39)
    if n=='1':
        displayList(Food)
    elif n=='2':
        displayList(Drinks)
    elif n=='3':
        displayList(Snack)
    else:
        print('Eror')
        opChoice()
def idk(n,Food,Drinks,Snack,Order):
        asnChoice(n,Food,Drinks,Snack)
        ipunt=input('What would you like to order? ')
        try:
            if n=='1':
                Order.append(Food[int(ipunt)-1])
            elif n=='2':
                Order.append(Drinks[int(ipunt)-1])
            elif n =='3':
                Order.append(Snack[int(ipunt)-1])
        except:
            input('Eror')
            idk(n,Food,Drinks,Snack,Order)
        lastChoice(Food,Drinks,Snack,Order)
def lastChoice(Food,Drinks,Snack,Order):
    ns=input(f'1.continue order\n2.cancel order\n3.exit and check out\nWhat would you like to do? ')
    if ns=='1':
        opChoice(Food,Drinks,Snack,Order)
    elif ns=='2':
            input('Order canceled')
    elif ns=='3':
        print('Thank you for your order')
        enddata(Order)
        exit('Come back soon!')
        
def enddata(Order):
    with open(f'{directorti}/order.txt','a') as file:
        file.write(datetime.now().strftime('%Y-%m-%d %H:%M') + '\n')
        for line in Order:
            file.write('|'.join(line) + '\n')