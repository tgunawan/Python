import os
import numpy as np
def clear():
    os.system('cls')

def hitung(num1,operator="",num2=0):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        return num1/num2
    elif operator=="sqrt":
        print(operator,num1,"=", np.sqrt(num1))
    else:
        return "error"

print(hitung(2,"+",3))
hitung(8,"sqrt")