#docstring
"""
Module untuk tes class / method / function
"""

import os,time,random


class functions:
    """
    This is a module that contains functions that can be used in other modules.
    """
    def clear(t:int = 0)-> None: # (t:int = 0)-> None adalah type hints
        """
        This function clears the terminal screen. It checks the operating system and uses the appropriate command to clear the screen.
        """
        time.sleep(t)
        os.system('cls' if os.name == 'nt' else 'clear')

def random_color() -> str:
    """
    This function generates a random color code in hexadecimal format.
    It returns a string representing the color code.
    """
    return f'#{random.randint(0, 0xFFFFFF):06x}'
    
def title(title:str, character: str) :
    """
    Put title in top of the terminal, center it and give it a decoration!

    :param title: The title that you want put to the screen terminal
    :param character: The special Character that you want to use for the decoration line
    """
    width = os.get_terminal_size ().columns

    if len (character) != 1:
        raise ValueError ("character must be one character")
    print (character * width)
    print (f' {character} {title:^{width-5}} {character} ')
    print (character * width)

def joinstr(*args,sep:str| None=" ") -> str:
    """
    This function takes any number of arguments and joins them into a single string.
    It returns the joined string.
    """
    return sep.join(map(str, args))