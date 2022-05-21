import sys
import tabulate

if (len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or open(sys.argv[1])