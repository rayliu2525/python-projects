import sys
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (splitext(lower(sys.argv[1]))[1] and splitext(lower(sys.argv[2]))[1]) not (.jpg or .jpeg or .png):
    sys.exit("Incorrect extensions")
elif splitext(lower(sys.argv[1]))[1] != splitext(lower(sys.argv[2]))[1]:
    sys.exit("Extensions are not the same")
elif sys.argv[1] not exists