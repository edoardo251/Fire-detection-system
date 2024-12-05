# File di funzioni
from colorama import Fore, Style, init

# Inizializza colorama
init()

class Functions:
    def validateType(type, param):
        if param is not None:
            if type == 'str':
                return isinstance(param, str)
            elif type == 'int':
                try:
                    int(param)  
                    return True
                except (ValueError, TypeError):
                    return False
            elif type == 'float':
                try:
                    float(param) 
                    return True
                except (ValueError, TypeError):
                    return False
            elif type == 'bool':
                return isinstance(param, bool)
            else:
                return False
        else:
            return False
        
    def printLine(color, text):
        color_code = getattr(Fore, color.upper(), Fore.WHITE)
        print(f"{color_code} {text} {Style.RESET_ALL}")