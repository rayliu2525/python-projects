import sys
import os
from PIL import image

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (os.splitext(lower(sys.argv[1]))[1] and os.splitext(lower(sys.argv[2]))[1]) not (.jpg or .jpeg or .png):
    sys.exit("Incorrect extensions")
elif os.splitext(lower(sys.argv[1]))[1] != os.splitext(lower(sys.argv[2]))[1]:
    sys.exit("Extensions are not the same")
elif not os.path.exists(sys.argv[1]):
    sys.exit("Input file does not exist!")

with image.open()