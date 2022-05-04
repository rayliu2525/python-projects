grocery_list = []

while True:
    try:
        item = input("Type item: ").upper()
    except EOFError:
        new_grocery_list = 
        quit()

    grocery_list.append(item)

