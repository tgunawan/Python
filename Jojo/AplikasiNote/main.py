#========================library========================#

import os

#========================variabel========================#

judulnote=[]
directorty='./Jojo/AplikasiNote'

#========================function========================#

def startData():
    with open(f'{directorty}/dataNote.txt', 'r') as file:
        for line in file:
            judulnote.append(line.strip())


def add(note):
    global judulnote
    os.system('cls')
    try:    
        with open(f'{directorty}/{note}.txt', 'x') as file:
            file.write(input("Enter your note: "))
            judulnote.append(note)
    except FileExistsError:
        input("This item is already in the list! ")
    else:
        displayList()
        enddata()

def remove(note):
    global judulnote
    os.system('cls')
    displayList()
    try:
        judulnote.remove(note)
        os.remove(f'{directorty}/{note}.txt')
    except ValueError:
        print("This item is not in the list! ")
    except FileNotFoundError:
        print(f'your note {note} does not exist! ')
    else:
        print(f'your note {note} has been deleted! ')
    displayList()

def displayList():
    print('====**NOTE**====')
    for i in range(len(judulnote)):
        print( i+1 , judulnote[i] )

def enddata():
    with open(f'{directorty}/dataNote.txt', 'w') as file:
        for line in judulnote:
            print(line)
            file.write(line + '\n')
def edit():
    os.system('cls')
    displayList()
    print(judulnote)
    try:
        note=judulnote[int(input("Select note to edit: "))-1]
    except IndexError:
        input("Note not found")
        edit()
    except ValueError:
        input("Insert a Note number")
        edit()
    else:
        with open(f'{directorty}/{note}.txt', 'w') as file:
            file.write(input("insert your new note: "))

#========================main========================#

# input(f'welcome to note app')
# input(f'here you can make note and remove note')
# input(f"Lets begin now")

startData()
# os.system('cls')
# displayList()
# input(f'to start lets begin by adding note')
# add(input("insert a new note to create: "))
# input(f'now lets remove note')  
# remove(input("Select note to remove: "))
# if input("do you want to add note or remove note") == 'add':
#     add(input("Select note to create: "))
# elif input("do you want to add note or remove note") == 'remove':
#     remove(input("Select note to remove: "))
edit()
enddata()