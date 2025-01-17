import textwrap
import numpy as np
text='Ini adalah contoh paragraf panjang. Ini kalimat ke dua, dari sebuah paragraf. Ini kalimat ketiga'
'''
print(text[0:5])
print(text[:4])
print(text[4:17])
print(text[4:])
print(text[-4:])'''# contoh simple slicing
print("="*50)
for word in range(0,len(text),30): # contoh pemotongan dengan slicing
    print('|',end='')
    print(text[word:word+30],end="")
    print('|')

print("="*50)
for i in range(0,len(text),30):
    print(f'|{text[i:i+30]:^30}|')

print("="*50)
# pembungkus=textwrap.TextWrapper(width=30)
# list=pembungkus.wrap(text)
# for element in list:
#     print(f'|{element:^30}|')

def printParagraf(text):
    pembungkus=textwrap.TextWrapper(width=30)
    list=pembungkus.wrap(text)
    for element in list:
        print(f'|{element:^30}|')

printParagraf("Test untuk Pragradf panjang apakah ini akan di sorting")