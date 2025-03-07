def format_angka(angka):
  return f"Rp {angka:,}"

# Contoh penggunaan
angka1 = 2000000
angka2 = 5000000000

angka_formatted1 = format_angka(angka1)
angka_formatted2 = format_angka(angka2)

print(f"{angka1:,} menjadi {angka_formatted1}")
print(f"{angka2} menjadi {angka_formatted2}")