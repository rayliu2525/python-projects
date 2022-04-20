x = input("Name of variable in camel case: ")
l = []
for letter in x:
    if isupper(letter) = True:
        l.append(f"_{letter.lower()})
    else:
        l.append(letter)
    return 