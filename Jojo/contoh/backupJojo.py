#===================Library===================#
import numpy as np
import os,time,textwrap
#===================Variable===================#
num1=0
num2=0
answer=0
Operator='+'
#===================Function===================#
def clear():
    os.system('cls')
def display(answer,Operator):
    clear()
    wraper=textwrap.TextWrapper(width=24)
    asn=wraper.wrap(f"{str(num1)}{Operator}{str(num2)}={str(answer)}")
    print('========Calculator========')
    for i in asn:
        print(f'|{i:^24}|')
    print('='*26)
def basicoperator():
    global num1,num2
    num1=int(input('Masukan angka pertama: '))
    num2=int(input('Masukan angka kedua: '))
    choice=input('1.add\n2.sub\n3.mul\n4.div\n5.advance choice\nMasukan pilihan anda: ')
    if choice=='add'or choice=='1':
        answer=np.add(num1,num2)
        Operator='+'
    elif choice=='sub'or choice=='2':
        answer=np.subtract(num1,num2)
        Operator='-'
    elif choice=='mul'or choice=='3':
        answer=np.multiply(num1,num2)
        Operator='X'
    elif choice=='div'or choice=='4':
        answer=np.divide(num1,num2)
        Operator=':'
    elif choice=='advance' or choice=='5':
        AdvancedChoice()
    display(answer,Operator)
def AdvancedChoice():
    choice=input('1.add\n2.sub\n3.mul\n4.div\n5.back\nMasukan pilihan anda: ')
#===================Main===================#
display(0,'+')
basicoperator()

