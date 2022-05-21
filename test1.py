import tabulate

with open("regular.csv") as regular:
    regular_list = []
    for l in regular:
        print l