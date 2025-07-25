import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x= np.random.rand(120,1) * 5
plt.figure(num="The powewer og love" ,figsize=(10,6))
plt.title("The Power of Love")
y=2*x+1+np.random.randn(120,1)*2
plt.plot(x, y , 'yo') 
plt.xlabel("Hari")
plt.arrow(0, 0, 1, 1, head_width=0.2, head_length=0.5, fc='blue', ec='blue') # panah

plt.show()

df_data=pd.DataFrame({'Data1': x.flatten(), 'y=Data2': y.flatten()}) # buat DataFrame / Dictionary dari data x dan y
print("\nDataFrame:\n", df_data)