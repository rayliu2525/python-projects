import sys

if len(sys.argv) == 2 and sys.argv[1][-3:] == ".py":
    with open(sys.argv[1]) as file:
        lines = [1 for line in file if (line.strip() and line.lstrip()[0] != "#")]
        sum_lines = sum(lines)
    print(sum_lines)

elif len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

elif sys.argv[1] == False or sys.argv[1][-3:] != ".py":
    print("file does not exist or is the wrong type")
    sys.exit(1)