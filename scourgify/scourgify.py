import csv
import sys

if len(sys.argv) not 3:
    sys.exit(1)

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    with open(sys.argv[2], w) as csv_file:
        csv_dictwriter = csv.DictWriter(csv_file, fieldnames=["first", "last", "house"])
            for row in csv_reader:
                first, last = split(row[0], ", ")
                csv_dictwriter.writerow({
                    "first": first,
                    "last": last,
                    "hosue": row[2]
                })