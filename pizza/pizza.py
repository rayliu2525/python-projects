import sys
import tabulate

try:
    if (len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or open(sys.argv[1]):
        sys.exit
    else:
        pizza_file_object = open(sys.argv[1])
        print(tabulate(pizza_file_object, headers, tablefmt="grid"))


except:
    sys.exit

