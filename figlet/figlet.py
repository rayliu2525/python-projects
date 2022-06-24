import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

font_list = figlet.getFonts()

if len(sys.argv) != 1:
    if len(sys.argv) != 3:
        sys.exit("1")

if ("-f" or "--font") not sys.argv[1] or sys.argv[2] not in font_list:
    sys.exit("1")

text = input("Input: ")


if len(sys.argv) == 1:
    figlet.setFont(font=(random.choice(font_list)))
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    figlet.setFont(font=(sys.argv[2]))
    print(figlet.renderText(text))