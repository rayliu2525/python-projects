grocery_list = []

while True:
    try:
        item = input("Type item: ").upper()
    except EOFError:
        new_grocery_list = []
        [new_grocery_list.append(x) for x in grocery_list if x not in new_grocery_list]
        new_grocery_list.sort()
        print()
        [print(f"{grocery_list.count(x)} {x}") for x in new_grocery_list]
        quit()

    grocery_list.append(item)

