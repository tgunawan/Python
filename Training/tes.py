import numpy as np
import pandas as pd

np.random.seed(42)

umur = np.random.randint(18, 60, 100)
income = np.random.randint(3, 15, 100) * 1_000_000
spending = np.random.randint(1, 100, 100)

df = pd.DataFrame({
    "Umur": umur,
    "Income": income,
    "Spending": spending
})

print(df.head())

X = df[["Umur", "Income", "Spending"]]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

