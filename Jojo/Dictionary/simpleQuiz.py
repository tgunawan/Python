#Quizz Game with Dictionary

#---------Libarary----------
import os # module librari os
import fungsi as f #module fungsi yang di buat sendiri


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
    
#---------Main----------
clear()

for soal in quiz:
    print(soal['pertanyaan'])
    jawaban=input('Jawaban: ')
    if jawaban==soal['jawaban']:
        score+=1
        f.wait(2)
        clear()
    else:
        life-=1
        print('Kamu salah')
        f.wait(2)
        clear()
        if life==0:
            print('Kamu kalah')
            break

if score==len(quiz):
    print('Selamat kamu benar semua')
print(f'Kamu benar {score} dari {len(quiz)} soal')
#---------End----------