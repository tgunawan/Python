"""
Module untuk tes class / method / function
"""
import os,time,random

class functions:
    """
    This is a module that contains functions that can be used in other modules.
    """
    def clear(t:int = 0)-> None:
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
    