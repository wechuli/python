from pyfiglet import figlet_format
from termcolor import colored
import colorama
colorama.init()


accepted_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan')


def print_art():
    msg = input("What would you want to print? ")
    color = input("What color? ")
    if color not in accepted_colors:
        color = 'cyan'
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


print_art()