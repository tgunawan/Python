import matplotlib.pyplot as plt
import numpy as np


'''#simple ploting line
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()'''

'''#simple ploting dot
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, 'o')
plt.show()'''

'''#marker with star
ypoints = np.array([3, 8, 1, 10])
#xpoints = np.array([0, 2, 3, 7])
#plt.plot(xpoints,ypoints, marker = '*')
plt.plot(ypoints, marker = '*')
plt.grid(True) #show grid
plt.show()'''

'''#Pemakaian diagram grafik
x = np.arange(0, 10, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()'''

'''#buat matrix2D dari 0 hingga n
def get_mat(n):
    data = np.arange(n)
    data = np.add.outer(data,data)
    return data

print(get_mat(10))''' 