import time,sys

waktu_mulai = time.time()  # Catat waktu mulai

def loading():
    listload = ["🌑", "🌘", "🌗", "🌖", "🌕", "🌔", "🌓", "🌒"]
    for pic in listload:
        print(f"\rLoading: {pic}{}", end="")  # \r returns cursor to the beginning of the line
        sys.stdout.flush()  # Forces output to be displayed immediately
        time.sleep(0.2)  # Adjust delay as needed
    print("\rLoading complete!     ") # Clear the loading animation and print a completion message

# Example usage:
loading()
print("Continuing with the program...")

waktu_selesai = time.time()  # Catat waktu selesai

selisih_waktu = waktu_selesai - waktu_mulai  # Hitung selisih waktu

print(f"Waktu yang dibutuhkan: {selisih_waktu:.2f} detik")