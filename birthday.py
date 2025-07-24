# Print statements examples with sweet style!
from colorama import init, Fore, Style
import sys
import time
import random

init(autoreset=True)

# Futuristic typing effect for ASCII Art Header
header = r"""
  ____            _       _           _   _           _ 
 |  _ \ ___  __ _(_) __ _| |__  _   _| |_(_) ___  ___| |
 | |_) / _ \/ _` | |/ _` | '_ \| | | | __| |/ _ \/ __| |
 |  _ <  __/ (_| | | (_| | | | | |_| | |_| |  __/\__ \_|
 |_| \_\___|\__, |_|\__,_|_| |_|\__,_|\__|_|\___||___(_)
            |___/                                       
"""
for char in header:
    sys.stdout.write(Fore.MAGENTA + Style.BRIGHT + char)
    sys.stdout.flush()
    time.sleep(0.002 if char != '\n' else 0.01)

# Glitch effect for welcome message
def glitch_text(text, colors, repeat=10, delay=0.03):
    for _ in range(repeat):
        color = random.choice(colors)
        sys.stdout.write('\r' + color + Style.BRIGHT + text)
        sys.stdout.flush()
        time.sleep(delay)
    print('\r' + Fore.CYAN + Style.BRIGHT + text)

glitch_text("Welcome!", [Fore.CYAN, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTBLUE_EX])

print(Fore.YELLOW + "1000")
print(Fore.GREEN + "a =", 100)

# Print a formatted, colorized table of names and ages
print(Fore.BLUE + Style.BRIGHT + "\nName     \tAge")
rows = [
    ("Jack", 15),
    ("John", 18),
    ("James", 13),
    ("Sam", 14),
    ("Bill", 15)
]
for name, age in rows:
    print(Fore.WHITE + f"{name:<8}\t{age}")

# Print two statements on the same line
print(Fore.LIGHTMAGENTA_EX + 'This is the first line', end=" ")
print(Fore.LIGHTCYAN_EX + "and it will be printed in the same line.")

# Sweet ending message
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "\nHave a SWEET day! \U0001F36C\U0001F36D\U0001F36B")
