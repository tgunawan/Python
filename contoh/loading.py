import time
import sys

def loading():
    listload = ["🌑", "🌘", "🌗", "🌖", "🌕", "🌔", "🌓", "🌒"]
    for pic in listload:
        print(f"\rLoading: {pic}", end="")  # \r returns cursor to the beginning of the line
        sys.stdout.flush()  # Forces output to be displayed immediately
        time.sleep(0.2)  # Adjust delay as needed
    print("\rLoading complete!     ") # Clear the loading animation and print a completion message

# Example usage:
loading()
print("Continuing with the program...")

# Or, for a more concise version using a loop counter:

def loading_concise():
    for i in range(8):  # Number of phases in the animation
        phase = "🌑🌘🌗🌖🌕🌔🌓🌒"[i] # Directly index the string
        print(f"\rLoading: {phase}", end="")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\rLoading complete!     ")

loading_concise()
print("Continuing with the program...")


#  Even more concise using itertools.cycle:

import itertools

def loading_itertools():
    phases = "🌑🌘🌗🌖🌕🌔🌓🌒"
    for phase in itertools.cycle(phases):
        print(f"\rLoading: {phase}", end="")
        sys.stdout.flush()
        time.sleep(0.2)
        break # Remove this break to make it loop indefinitely. Add a condition to stop it.
    print("\rLoading complete!     ")

loading_itertools()
print("Continuing with the program...")
#========== Library ===========
import os, time, sys

#========== Variable ==========


#========== Function ==========
def clear():
    os.system('cls')
def loading(ulang):
    listload = ["🌑", "🌘", "🌗", "🌖", "🌕", "🌔", "🌓", "🌒"]
    for i in range(ulang):
        for pic in listload:
            print(f"\rLoading: {pic}")
            time.sleep(0.2)  # Adjust delay as needed
            clear()
    print("\rLoading complete!     ")
#========== Main ==============
loading(4)
#========== End ===============

# Dokumentasi
# https://docs.python.org/3/library/itertools.html

# https://docs.python.org/3/library/time.html

# https://docs.python.org/3/library/sys.html

# https://docs.python.org/3/library/os.html