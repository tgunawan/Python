# """
# This file (as well as requirements.txt) has been kept to make sure the original instructions illustrated in the demonstration video are still valid.
# This script is simply a hack to make it seem like `python -m auto_py_to_exe` was called when `python run.py` is executed.
# """

# from auto_py_to_exe import __main__ as apte

# apte.__name__ = '__main__'
# apte.run()

import os
print(f'| {"hello, please fill in the form":<40} |')
print('-'*44)

aa= input(f'|{"what is ur name?":^31} |')
age=int(input(f'|{"what is your age?":^31}| '))
hobby= input(f' |{"what is yout hobby":^31}| ')
food=input(f'| {"what is ur perfered food?":^31} | ')
future=input(f'| {"what do u wawnt in the future":^31}| ')
input('-'*44)
os.system("clear")

print("-"*46)
print(f'|{ 1 }| {"my name is":<24}|{aa:^15} |')
print(f'|{ 2 }| {"my age is":<24}|{age:^15}|')
print(f'|{ 3 }| {"my hobby is":<24}|{hobby:^15}|')
print(f'|{ 4 }| {"my favorite food is":<24} |{food:^15}|')
print(f'|{ 5 }| {"my future is going to be":<24} |{future:^15}|')
print("_"*46)