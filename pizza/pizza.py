import sys
import tabulate
import csv
import os.path

try:
    if (len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1])):
        sys.exit
    else:
        with open(sys.argv[1], "r") as regular:
            csv_reader = csv.reader(regular)
            regular_list = []
            for row in csv_reader:
                regular_list.append(row)
            print(tabulate(regular_list, headers=["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))


except Exception as e:
    print("e")
    sys.exit

