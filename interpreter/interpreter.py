answer = input("expression: ")
x, y, z = answer.split(" ")
if y == "+":
    f = float(int(x) + int(z))
    format_float = "{:.1f}".format(f)
elif y == "-":
    print(int(x) - int(z))
elif y == "*":
    print(int(x) * int(z))
elif y == "/":
    print(int(x) / int(z))