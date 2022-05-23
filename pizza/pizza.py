import sys
import tabulate
import csv
import os.path

try:
    if (len(sys.argv) != 2 or sys.argv[1][-4:] != ".csv" or not os.path.exists(sys.argv[1])):
        sys.exit(1)
    else:
        with open(sys.argv[1], "r") as regular:
            csv_reader = csv.reader(regular)
            regular_list = []
            for row in csv_reader:
                if csv_reader[row] != ["Regular Pizza", "Small", "Large"]:
                    regular_list.append(row)
            print(tabulate.tabulate(regular_list, headers=["Regular Pizza", "Small", "Large"], tablefmt="grid"))


except:
    sys.exit(1)

