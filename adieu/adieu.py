import inflect
p = inflect.engine()

name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        break

print("")
for name in name_list:
    print(f"Adieu, adieu, to {p.join(name_list[:(name_list.index(name) + 1)])}")
