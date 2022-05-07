import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

font_list = figlet.getFonts()

if (-f or -font) not in sysargv[1] or font_list not in sysargv[2]:
    sys.exit



text = input("Input: ")

if len(sys.argv) == 1:
    figlet.setFont(random.choice(font_list))
    print(figlet.renderText(text))

if len(sys.argv) == 3:
    figlet.setFont(random.choice(sys.argv[2]))
    print(figlet.renderText(text))
