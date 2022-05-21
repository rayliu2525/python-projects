import tabulate
import csv

with open("regular.csv", "r") as regular:
    csv_reader = csv.reader(regular)
    regular_list = []
    for row in csv_reader:
        regular_list.append(row)

print(regular_list)