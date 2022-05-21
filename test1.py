import tabulate
import csv

with open("regular.csv", "r") as regular:
    csv_reader = csv.reader(regular)

    print(csv_reader)