answer = input("expression: ")
x, y, z = answer.split(" ")
if y == "+":
    print(int(x) + int(z))
elif y == "-":
    print(int(x) - int(z))
elif y == "*":
    print(int(x) * int(z))
elif y == "/":
    print(int(x) / int(z))