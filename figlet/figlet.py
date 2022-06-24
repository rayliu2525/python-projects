import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

font_list = figlet.getFonts()



text = input("Input: ")

if len(sys.argv) == 1:
    figlet.setFont(font=(random.choice(font_list)))
    print(figlet.renderText(text))

if len(sys.argv) == 3:
    figlet.setFont(font=(sys.argv[2]))
    print(figlet.renderText(text))

if ("-f" or "-font") not in sys.argv[1] or sys.argv[2] not in font_list:
    sys.exit()

if len(sys.argv) not 1:
    sys.exit()

if len(sys.argv) not 3:
    sys.exit()