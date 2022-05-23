import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    with open(sys.argv[2], w) as csv_file:
        csv_dictwriter = csv.DictWriter(sys.argv[2], fieldnames=["first", "last", "house"])
            for row in csv_reader:
                first, last = split(row[0], ", ")
                csv_dictwriter.writerow({
                    "first": first,
                    "last": last,
                    "hosue": row[2]
                })