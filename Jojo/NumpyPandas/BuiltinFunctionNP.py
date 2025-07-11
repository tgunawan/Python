#builtin Function
import numpy as np

# Array of zero
array_zero = np.zeros((3, 4)) # 3 Baris, 4 kolom
print("Array of zero:")
print(array_zero)

# Array of ones
array_ones = np.ones((5, 2)) # 5 Baris, 2 kolom
print("Array of ones:")
print(array_ones)

# Array with constant value
fullArray = np.full((2,3),"Jojo")
print("\n Full Array (2x3) with constant value 7:")
print(fullArray)

# identity Matrix => Square matrix dengan garis diagonal 1
identity_matrix = np.eye(4) # 4x4 
print("\n Identity Matrix (4x4):")
print(identity_matrix)

# Array with range of numbers
array_range = np.arange(10) # 0-9
print("\n Array with range of numbers (0-9):")
print(array_range)

rangeArray = np.arange(5, 15) # 5-14
print("\n Range Array (5-14):")
print(rangeArray)

stepArray = np.arange(0, 20, 2) # 0-18 step 2
print("\n Step Array (0-18 step 2):")
print(stepArray)

# Linear space numbers
linearArray = np.linspace(0, 10, 6) # 5 numbers from 0 to 10
print("\n Linear Array (0-10, 5 numbers):")
print(linearArray)
