import subprocess,os

# contoh = subprocess.run(["python", "contoh/decorator.py"], capture_output=True)
# print(contoh.stdout.decode())

# contoh="contoh/" #folder contoh
# jojo="jojo/" #folder jojo
# subprocess.run(["python", contoh+"decorator.py"])

import random
from collections import defaultdict

text = "saya suka makan nasi goreng saya suka minum teh"

os.system("cls" if os.name == "nt" else "clear")
# Buat model transisi kata
words = text.split()
model = defaultdict(list)
for i in range(len(words)-1):
    model[words[i]].append(words[i+1])

# Generator kalimat
word = "saya"
sentence = [word]

for _ in range(10):
    if not model[word]:  # kalau tidak ada next word
        break
    next_word = random.choice(model[word])
    sentence.append(next_word)
    word = next_word

print(" ".join(sentence))
