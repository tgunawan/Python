#----------library----------
import os,time
import datetime as dt

#----------variable----------
directory='./Jojo/Feedback/Console'



#----------function----------
def bacaData():
    try:
        with open(f'{directory}/feedback.txt','r') as file:
            return file.readlines()
    except FileNotFoundError:
        with open(f'{directory}/feedback.txt','w') as file:
            return []
    
def displayData():
    if not daftarFeedback:
        print('Belum ada Feedback')
    else:
        print('Daftar Feedback:')
        for fb in daftarFeedback:
            print(fb.strip())


#----------main----------
while True:
    os.system('cls')
    print(f'{"Selamat datang di Feedback Form App":^50}')
    print('''Menu Feedback:
1. Display Current Feedback
2. Tulis Feedback baru
3. Exit App''')
    pilih=int(input('Masukkan pilihan(1-3): '))
    daftarFeedback=bacaData()
    displayData()


    nama=input(f'{"Masukkan nama:":<25} ')
    email=input(f'{"Masukkan Email:":<25} ')
    umpanBalik=input(f'{"Masukkan Feedback anda:":<25} ')

    if not nama or not email or not umpanBalik:
        input("Peringatan: semua item harus di isi!!!")
        continue
    else: 
        try:
            with open(f'{directory}/feedback.txt','a') as file:
                waktu=dt.datetime.now().strftime("%d-%m-%Y\t%H:%M:%S")
                file.write(f'Waktu: {waktu}\n')
                file.write(f'Nama: {nama}\n')
                file.write(f'email: {email}\n')
                file.write(f'Note: {umpanBalik}\n')
                file.write(f'{"="*50}\n')
            print('Terimakasih atas Feedback anda')
            time.sleep(2)
        except Exception as e:
            print('Terjadi error',e)
#----------end----------