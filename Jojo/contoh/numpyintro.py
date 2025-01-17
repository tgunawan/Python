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