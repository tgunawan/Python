#Quizz Game with Dictionary

#---------Libarary----------
import os
import time
#---------Variable----------
quiz=[
    {
        'pertanyaan': 'Apa nama ibu kota Indonesia?',
        'jawaban': 'Jakarta'
    },
    {
        'pertanyaan': 'Berapa detik dalam 1 Jam?',
        'jawaban': '3600'
    }
    
]
score=0
life=5
#---------Function----------    
def clear():
    os.system('cls')
    
def wait(sec):
    time.sleep(sec)
#---------Main----------
clear()

for soal in quiz:
    print(soal['pertanyaan'])
    jawaban=input('Jawaban: ')
    if jawaban==soal['jawaban']:
        score+=1
        wait(2)
        clear()
    else:
        life-=1
        print('Kamu salah')
        wait(2)
        clear()
        if life==0:
            print('Kamu kalah')
            break
        
if score==len(quiz):
    print('Selamat kamu benar semua')
print(f'Kamu benar {score} dari {len(quiz)} soal')
#---------End----------