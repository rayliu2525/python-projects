import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        first, last = split(row[0], ", ")