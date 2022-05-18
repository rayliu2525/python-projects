import sys

if sys.argv == 2 and sys.argv[1] == .py:
    with open(sys.argv[1]) as file:
        lines = [1 for line in file if (line.rstrip() and line[0] != \#)]
        sum_lines = sum(lines)
    print(sum_lines)

