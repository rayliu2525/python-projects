import sys
import os
import PIL

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

with PIL.image.open(sys.argv[1]) as input_image:
    PIL.ImageOps.fit(input_image, sys.argv[2].size)