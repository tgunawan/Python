import os,time
import module as md

text = "Welcome to Bookworms!"
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.2)


'''print("\nWhat brings you here today?")
md.functions.clear()
print("1. Add a book\n2. See the books\n3. Edit the books\n4. Remove a book\n5. Buy a book(coming soon maybe)")
print(md.random_color())
md.title("Bookworms", "*")
listbuah=["jambu","apel","mangga","pisang"]
print(md.joinstr(*listbuah,sep=", ")) # jika list pakai * diambil valuenya, jika langsung tetap jadi list
print("Selamat datang","di sana",sep="-")
print(*listbuah,sep=" - ")
nama={"detail": {"Nama": "Tedi", "Umur": 20, "Alamat": "Bandung"}}
# nama=["Tedi", "Dedi", "Budi"]
print(*nama["detail"],*nama["detail"].values(),sep="-") # *nama["detail"] mengambil key, *nama["detail"].values() mengambil value    
nama = 'Kevin'
print(*[nama]*4,sep=' - ')
 
'''