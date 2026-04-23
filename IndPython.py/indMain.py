from indfunc import *
from varNob import *

''' fungsi yang tidak bisa di terjemahkan
if
else
for
while
class
def
return'''
tulis(nama)
tulis("Welcome to IndPython.")


tulis("=== MINI PYTHON INDONESIA ===")

nama = masukan("Masukkan nama: ")
umur = angka(masukan("Masukkan umur: "))

if umur > 17:
    tulis("Halo", nama, "- Kamu sudah dewasa")
else:
    tulis("Halo", nama, "- Kamu masih muda")