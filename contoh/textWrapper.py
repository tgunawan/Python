import textwrap

teks = """
Ini adalah contoh teks yang sangat panjang yang akan kita bungkus menggunakan modul textwrap di Python. 
Tujuannya adalah agar teks ini tidak melebihi lebar tertentu.
"""

# Membungkus teks dengan lebar 40 karakter
teks_dibungkus = textwrap.fill(teks, width=40)
print(teks_dibungkus)