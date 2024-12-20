#------------library------------
import os
import time
import fungsi as f

#------------variable------------
ListMenu = []
directory='./Jojo/Cafe'
#------------function------------
def GetData(directory):
    with open(f'{directory}/dataCafe.txt', 'r') as file:
        for line in file:
            ListMenu.append(line.strip())

def enddata():
    with open(f'{directory}/dataCafe.txt', 'w') as file:
        for line in ListMenu:
            # print(line)
            file.write(line + '\n')


#------------main------------
GetData(directory)
print(ListMenu)
for i in range(len(ListMenu)):
    print(ListMenu[i])

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