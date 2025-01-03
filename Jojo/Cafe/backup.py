#===========================library==================#
import os,time,random
from datetime import datetime
import handsomecode as hc
#===========================Variable==================#
directorti='./HandsomeCafe'
Order=[]
Food=[]
Drinks=[]
Snack=[]
#===========================Function==================#
#indefernfile #awsome #compect #slay
#===========================Main==================#
hc.startData('Food',Food)
hc.startData('Drinks',Drinks)
hc.startData('Snack',Snack)
print(Food)
print(Drinks)
print(Snack)
#print(Menu)
# input('Welcome to Handsome Cafe')
# input('Ici, nous vous servons avec des aliments de la plus haute qualité.')
# input('What Can We Serve You Today?')
#os.system('cls')
while True:
    n=input('1.Order\n2.Exit\nWhat would u like to do? ')
    os.system('cls')
    if n=='1':
        hc.opChoice(Food,Drinks,Snack,Order)
    elif n=='2':
        exit('Have a nice day!')

