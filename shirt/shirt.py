import sys
import os
import PIL

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

with PIL.Image.open(sys.argv[1]) as input_image:
    PIL.ImageOps.fit(input_image, sys.argv[2].size)
    overlay_image = input_image.paste(shirt.png)
    overlay_image.save(sys.argv[2])