import tabulate

with open("regular.csv") as regular:
    print(tabulate(regular, headers=["Regular Pizzar", "Small", "Large"], tablefmt="grid"))