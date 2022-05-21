import tabulate

with open("regular.csv") as regular:
    regular_list = []
    for l in regular:
        regular_list.append(l)

    print(tabulate(regular, headers=["Regular Pizzar", "Small", "Large"], tablefmt="grid"))



make list of lists from regular