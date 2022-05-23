import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    with open(sys.argv[1], w) as csv_file:
        csv_dictwriter = csv.DictWriter

    for row in csv_reader:
        first, last = split(row[0], ", ")