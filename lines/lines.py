import sys

if sys.argv == 2 and sys.argv[1] == .py:
    with open(sys.argv[1]) as file:
        lines = [1 for line in file if (line.rstrip() and line[0] != \#)]
        sum_lines = sum(lines)
    print(sum_lines)

if sys.argv < 2:
    print("Too few command-line arguments")
    sys.exit()

elif sys.argv >2:
    print("Too many command-line arguments")

elif sys.argv[1] == False or sys.argv[1] != .py