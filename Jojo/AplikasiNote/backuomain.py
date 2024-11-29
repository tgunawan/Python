#==============Library================
import os

#==============Variable================
judulnote=["tes","tes2"]
directory='./Jojo/AplikasiNote'
#==============Function================
def startData():
    with open(f'{directory}/dataNote.txt', 'r') as f:
        for line in f:
            judulnote.append(line.strip())

def add(note):
    with open(f'{directory}/{note}.txt', 'x') as f:
        f.write(input("Enter note: "))
        judulnote.append(note)
    displayList()

def remove(note):
    displayList()
    try:
        judulnote.remove(note)
        os.remove(f'{directory}/{note}.txt')
    except ValueError:
        input("Note not found")
    else:
        input(f'{note} Note has been removed')
        displayList()

def displayList():
    os.system('cls')
    print('====**NOTE**====')
    for i in range(len(judulnote)):
        print( i+1 , judulnote[i] )

def EndData():
    with open(f'{directory}/dataNote.txt', 'w') as f:
        # print(judulnote)
        for line in judulnote:
            # print(line)
            f.write(line + '\n')
#==============Main================


if __name__ == '__main__':
    startData()
    print(judulnote)
    input()
    displayList()
    add(input("Select note to enter: "))
    remove(input("Select note to remove: "))
    EndData()