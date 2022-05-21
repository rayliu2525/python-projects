import tabulate

with open("regular.csv", "r") as regular:
    regular_list = []
    for l in regular:
        regular_list.append(l)

print(regular_list)

print(tabulate(regular_list, headers=["Regular Pizzar", "Small", "Large"], tablefmt="grid"))