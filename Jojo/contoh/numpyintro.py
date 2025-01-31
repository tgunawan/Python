import numpy as np
import os

os.system('cls')
list=["test",3,True]
# buat array
array1=np.array([6,7,8])
array2=np.array([[1,2,3],[3,4,5]])

# print(array2)

# operator
print(array1*2)
print(array1*array2)

#akses
print(array1[1])
print(array2[0][1])

#fungsi numpy statistik
print(np.mean(array1))
print(np.max(array1))
print(np.min(array1))

#fungsi Reshaping
array2=array2.reshape(1,6)
print(array2)
array2=array2.reshape(3,2)
print(array2)

# array1=array1.reshape(3,1) # error tidak dapat reshape 1D

#fungsi random
random_array2d=np.random.rand(3,3)
print(random_array2d)

random_array1d=np.random.rand(5)
print(random_array1d)
num1=3
num2=4
num3=81
num4=90
os.system('cls')
# np.add(array1,array2)
# np.subtract(array1,array2)
# np.divide(array1,array2)
# np.multiply(array1,array2)
print(np.power(num1,num2)) # pangkat3^4 / num1 ^ num2
print(np.sqrt(num3))# akar kuadrat
print(np.log(num3))# log
print(np.log10(100000))# log10
print(np.sin(num4))# sin
print("log10",np.cos(num4))# cos
print(np.tan(num4))# tan
print(np.exp(1))# eksponen
print(round(np.pi,3))
