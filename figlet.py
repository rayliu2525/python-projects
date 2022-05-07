import random
import sys
from pyfiglet import Figlet
figlet = Figlet()

font_list = figlet.getFonts()

text = input("Input: ")

if len(sys.argv) = 1:
    figlet.setFont(random.choice(font_list))
