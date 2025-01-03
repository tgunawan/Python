import os
def clear():
    os.system('cls')

def GetData(directory,menu,List):
    with open(f'{directory}/{menu}.txt', 'r') as file:
        for line in file:
            List.append(line.strip())