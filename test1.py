import tabulate
import csv

with open("regular.csv") as regular:
    regular = csv.reader(regular)
    for row in regular:
        print(row)