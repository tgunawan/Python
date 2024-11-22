# Memorize Game

#------ Library------
import os
import random
import time

#--------Variable------
hewan=['horse','cat','dog','elephant','lion','tiger','monkey']
score=0
n=1
jumlah_hewan=3 #maks 7 = 3,5,7


#--------Function------
def display(list):
    for i in list:
        print(i)

def awal():
    os.system('cls')
    input(f"""          Memorize Game
- input animal name in correct order
- game ada 3 level
- score dimulai dari 0
- jika salah score akan di kurangi
Press Enter to continue""")
    
def main():
    global n, jumlah_hewan, score
    while n<=3:
        os.system('cls')
        print(f'Level {n}')
        listBenar=random.sample(hewan,jumlah_hewan)
        listAcak=listBenar.copy()
        random.shuffle(listAcak)

        display(listBenar)
        time.sleep(5)
        os.system('cls')

        index=0
        while True:
            os.system('cls')
            print(f'Score= {score}')
            display(listAcak)
            jawab=input(f'Jawab: ').lower()
            if jawab==listBenar[index]:
                listAcak.remove(jawab)
                index+=1
                score+=10
                if len(listAcak)==0:
                    jumlah_hewan+=2
                    break
            else:
                score-=5
                input(f'Jawaban anda salah\n press enter to continue')
                if score<0:
                    score=0
                    quit("Game Over")

        print(f'Score= {score}')

        n+=1
#--------Main--------
awal()
main()

#--------End--------
