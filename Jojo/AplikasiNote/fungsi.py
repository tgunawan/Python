

def startData(directorty,judulnote):
    with open(f'{directorty}/dataNote.txt', 'r') as file:
        for line in file:
            judulnote.append(line.strip())