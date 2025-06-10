import numpy as np
import os

def clear():
    # Clear the console
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#example 1    
clear()
array1=np.array([6,7,8])
array2=np.array([[1,2,3],[3,4,5]])

print(array1*2)
print(array1*array2)

#example 2
clear()

array2=array2.reshape(1,6)
print(array2)
array2=array2.reshape(3,2)
print(array2)