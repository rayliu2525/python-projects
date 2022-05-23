import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)