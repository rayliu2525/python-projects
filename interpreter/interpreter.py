answer = input("expression: ")
x, y, z = answer.split(" ")
if y == "+":
    f = float(int(x) + int(z))
    q = "{:.1f}".format(f)
    print(q)
elif y == "-":
    f = float(int(x) - int(z))
    q = "{:.1f}".format(f)
    print(q)
elif y == "*":
    f = float(int(x) * int(z))
    q = "{:.1f}".format(f)
    print(q)
elif y == "/":
    f = float(int(x) / int(z))
    q = "{:.1f}".format(f)
    print(q)