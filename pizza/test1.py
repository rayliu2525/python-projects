import tabulate
import csv

try:
    with open("regular.csv", "r") as regular:
        csv_reader = csv.reader(regular)
        regular_list = []
        for row in csv_reader:
            regular_list.append(row)
except:
    print("wrong")
finally:
    print("w/e")

print(regular_list)