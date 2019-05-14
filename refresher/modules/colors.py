import termcolor
# or
from termcolor import colored, cprint
import colorama

colorama.init()




text = termcolor.colored(
    'Hi there Wechuli', color="yellow", on_color="on_magenta",attrs=["blink"])

print(text)

cprint('Hi', color='red', attrs=["blink"])
