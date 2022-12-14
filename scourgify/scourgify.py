import csv
import sys
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many comannd-line arguments")
if not os.access(sys.argv[1], os.R_OK):
    sys.exit(f"Could not read {sys.argv[1]}")


with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    with open(sys.argv[2], "w") as csv_file:
        csv_dictwriter = csv.DictWriter(csv_file, fieldnames=["first", "last", "house"])
        csv_dictwriter.writeheader()
        for row in csv_reader:
            last, first = row[0].split(", ")
            csv_dictwriter.writerow({
                "first": first,
                "last": last,
                "house": row[1]
            })