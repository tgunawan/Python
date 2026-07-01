import os,time
import module as md

text = "Welcome to Bookworms!"
for char in text:
    print(char, end="", flush=True)
    time.sleep(0.2)

print("\nWhat brings you here today?")
md.functions.clear()
print("1. Add a book\n2. See the books\n3. Edit the books\n4. Remove a book\n5. Buy a book(coming soon maybe)")
print(md.random_color())
