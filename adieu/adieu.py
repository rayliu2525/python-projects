name_list = []

while True:
    try:
        name = input("Name: ")
        name_list += name
    except EOFError:
        break


