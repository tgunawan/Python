import numpy as np
# print(np.__version__)
#beda list dan Array

# 1D list != 1D Array
list1D = [1, 2, 3, 4, 5]
list2D = [[1, 2, 3], [4, 5, 6]]
list3D = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
array1D = np.array(list1D)
array2D = np.array(list2D)
array3D = np.array(list3D)
print("1D Array :", array1D , list1D)
print("Shape:", array1D.shape) # (5,) => 5 element, 1 Dimensi #=> Vector

print("2D Array :", array2D)
print("2D List :", list2D)
print("Shape:", array2D.shape) # (2, 3) # 2 Dimensi, 2 baris, 3 kolom #=> Matrix

print("3D Array :", array3D)
print("3D List :", list3D)
print("Shape:", array3D.shape) # (2, 2, 2) # 3 Dimensi, 2 baris, 2 kolom, 2 kedalaman #=> Tensor
# 1 2 3 # baris 1
# 4 5 6 # baris 2

# 1 2 # baris 1
# 3 4
# 5 6 # baris 2
# 7 8