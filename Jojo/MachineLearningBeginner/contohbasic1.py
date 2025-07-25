import matplotlib.pyplot as plt

plt.figure(num='My Plot', figsize=(10, 6))

plt.plot([1, 2, 3, 4], [10, 8, 12, 6])
plt.title("Grafik Penjualan")
plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.show()