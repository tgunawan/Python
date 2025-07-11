import numpy as np

array1= np.array([1, 2, 3, 4,5,6])
array2= np.array([5, 6, 7, 8,9,10])

# Basic operations Array in numpy
'''
addition = array1 + array2 # element-wise addition
print("Addition of two arrays:",addition)
print("Multiplication of two arrays:", array1 * array2) #element-wise multiplication

arrat1= array1*5
print("Scalar multiplication",arrat1) #scalar multiplication
exponesial = array1 ** 2 #element-wise exponentiation
print("Exponential of array1:", exponesial)

# array1.append(5) #list
# array1 = np.append(array1, 5)  # Append 5 to array1
# print("Array after appending 5:", array1)
# addition = array1 + array2
# print("Addition of two arrays:",addition) #error karena beda jumlah data
'''
array1=array1.reshape(3, 2) # Reshape array1 to 2 baris x 2 kolom
print("Reshaped array1 to 3x2:",array1)



# Aggregation functions (Function for calculating statistics  Summarize data)
'''#sum,mean,max,min,std
print("Sum of array1:", np.sum(array1)) # Sum of all elements
print("Mean of array1:", np.mean(array1)) # Mean of all elements
print("Max of array1:", np.max(array1)) # Maximum value
print("Min of array1:", np.min(array1)) # Minimum value
print("Standard Deviation of array1:", np.std(array1)) # Standard deviation

print("Sum of each column in array1:", np.sum(array1, axis=0)) # Sum of each column
print("Mean of each row in array1:", np.sum(array1, axis=1))'''

# Slicing and indexing
'''my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_array = my_array*10
print(my_array)

print("Elemen at (0,1):", my_array[0, 1])  # Accessing element at row 0, column 1
print("Elemen at row (0):", my_array[0])  # Accessing entire row 0
print("Elemen at kolom (1):", my_array[:,1]) # Accessing entire column 1
#print baris 1 dan 2 juga kolom 2 dan 3
print(my_array[0:2,1:3]) #seperti angka pada for, belakang tidak di hitung
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]'''

# reshape and broadcasting
'''flatArray= np.arange(1, 13) # 1-12
NotflatArray= flatArray.reshape(4,3)
print("Flat Array (1-12):",NotflatArray)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(NotflatArray+5) # Broadcasting: adding 5 to each element in NotflatArray
vector = np.array([1, 2, 3]) # 1x3 vector
print("Ditambahkan Vector (1x3):\n", vector+NotflatArray) # Broadcasting: adding vector to each row of NotflatArray
'''

# Buat array 2D dan coba print beberapa operasi agregasi dan slice

random_array = np.random.randint(1, 100, size=(4, 5))  # 4x5 array dengan nilai acak antara 1 dan 100
print("\nRandom Array (4x5):", random_array)
# filter nilai yang lebih besar dari 50
filtered_array = random_array[random_array > 50]
print("Filtered Array (nilai > 50):", filtered_array)
#mengurutkan nilai dari array
sorted_array = np.sort(random_array, axis=None)  # Sort all elements in the array
print("Sorted Array (semua elemen):", sorted_array) 