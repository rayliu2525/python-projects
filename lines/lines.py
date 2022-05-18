import sys

with open(sys.argv[1]) as file:
    lines = [1 for line in file if (line.rstrip() and line[0] != #)]
    sum_lines = sum(lines)