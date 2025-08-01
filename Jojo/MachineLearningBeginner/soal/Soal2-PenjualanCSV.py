#------------ Import Libraries ------------
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#------------ Set Variables ------------
Directory = "Jojo/MachineLearningBeginner"


#------------ Function ------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#------------ Main Code ------------
df= pd.read_csv(f"{Directory}/DataDummy.csv" , sep=';')
print("\nData Dummy:\n", df)
