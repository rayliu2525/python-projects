grocery_list = []

while True:
    try:
        item = input("Type item: ").upper()
    except EOFError:
        
        quit()

    grocery_list.append(item)

