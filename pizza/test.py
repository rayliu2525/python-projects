import tabulate

with open("regular.csv") as regular:
    print(tabulate(regular, headers=["Regular Pizzar", "Small", "Large"], tablefmt="grid"))



make list of lists from regular