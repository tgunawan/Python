import sys
class bcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    CORRECT = "\033[32m"
    White = "\033[97m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    ENDC = '\033[0m'

def printc(color, text):
    print(color + text+bcolors.ENDC)

printc(bcolors.Cyan, sys.argv[0])
print(bcolors.WARNING + "hi")
print(bcolors.FAIL + "hi")
print(bcolors.CORRECT + "hi")
print(bcolors.White + "hi")
print(bcolors.Yellow + "hi")
print(bcolors.Blue + "hi")
print(bcolors.Magenta + "hi")
print(bcolors.Cyan + "hi")
print(bcolors.LightGray + "hi")
print(bcolors.DarkGray + "hi")
print(bcolors.LightRed + "hi")
print(bcolors.LightGreen + "hi")
print(bcolors.LightYellow + "hi")
print(bcolors.LightBlue + "hi")
print(bcolors.LightMagenta + "hi")
print(bcolors.LightCyan + "hi")