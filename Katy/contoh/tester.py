import random

angkaRahasia=random.randint(1,10) # 5
jawaban=0 # 4
guess=0

# Selama 4 tidak sama dengan 5:
while jawaban!=angkaRahasia: # !=, ==, >, <, ~, >=,<= 
    jawaban=int(input(''))
    guess+=1
    
    if jawaban<angkaRahasia:
        print('terlalu rendah / kedikitan')
    elif jawaban>angkaRahasia:
        print('terlalu besar / kebanyakan')
    else:
        print(f'Selamat anda benar, anda menebak {guess} kali')