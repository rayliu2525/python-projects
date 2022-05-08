import inflect

name_list = []

while True:
    try:
        name = input("Name: ")
        name_list += name
    except EOFError:
        break

for name in name_list:
    print(f"Adieu, adieu, to {inflect.join(name_list[:(name_list.index(name) + 1)])})
