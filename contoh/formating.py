import os,time, threading

def clear():
    os.system('cls')

def wait(waktu):
    time.sleep(waktu)

def loading():
    for i in range(10):
        print(f'\rHallo ke {i+1}',end='')
        #print(f'{"*"*i}',end='')
        wait(1)
    print('finish')

while True:
    loading()