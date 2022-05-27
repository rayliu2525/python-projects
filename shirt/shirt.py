import sys
import os
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif os.path.splitext(sys.argv[1])[1].lower() not in (".jpg", ".jpeg", ".png") and os.path.splitext(sys.argv[2])[1].lower() not in (".jpg", ".jpeg", ".png"):
    sys.exit("Incorrect extensions")
elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
    sys.exit("Extensions are not the same")
elif not os.path.exists(sys.argv[1]):
    sys.exit("Input file does not exist!")

with Image.open(sys.argv[1]) as input_image:
    with Image.open("shirt.png") as shirt_image:
        ImageOps.fit(input_image, shirt_image.size)
        input_image.paste(shirt_image)
        input_image.save(sys.argv[2])