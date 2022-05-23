import sys
import tabulate
import csv

regular_list = []


with open("regular.csv", "r") as regular:
    csv_reader = csv.reader(regular)
    for row in csv_reader:
        regular_list.append(row)

print(tabulate(regular_list, headers=["Sicilian Pizza", "Small", "Large"], tablefmt="grid"))