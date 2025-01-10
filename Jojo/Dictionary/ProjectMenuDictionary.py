#-----------Library------------#
import os

#-----------Variable------------#
menu={'Nasi Goreng':10000,
    'Ayam Goreng':15000,
    'Mie Goreng':15000,
    'Bakso':10000}
listmenu=[]

#-----------Function------------#
def clear():
    os.system('cls')

#-----------Main---------------#
clear()
for i in menu:
    listmenu.append(i)
    print(f'{i} {menu[i]}')

for i in range(len(listmenu)):
    print(f'{i+1}. {listmenu[i]} {menu[listmenu[i]]}')

# for i in range(len(menu)): tidak bisa pakai range untuk dictionary
#      print{menu[i+1]}')
    

print(menu)
print(menu.values)
#-----------End---------------#