# install scikit-learn
# pip install scikit-learn
# pip install matplotlib

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # untuk visualisasi data

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

np.random.seed(42) # set seed untuk reproducibility

#generate nilai x
x=np.random.rand(100,1) * 10 # 100 data acak antara 0-10
# print(x)

#generate nilai y dengan linear relation dengan x
y= 2*x+1+np.random.randn(100,1)*2 # y = 2x + 1 + noise

plt.figure(num="contoh 1" ,figsize=(10, 6)) # jendela ukuran 10x6 pertama kali buat paling atas

plt.title('Scatter Plot of Random Data') # judul tabel
plt.scatter(x,y, color='blue', label='RandomDataGenerated') # tampilan tabel dot scatter
plt.xlabel('X-axis Label') # label sumbu x
plt.ylabel('Y-axis Label') # label sumbu y
plt.legend() # informasi data
plt.grid(True) # grid pada tabel
plt.show()

df_data=pd.DataFrame({'x': x.flatten(), 'y': y.flatten()}) # buat DataFrame / Dictionary dari data x dan y
print("\nDataFrame:\n", df_data)