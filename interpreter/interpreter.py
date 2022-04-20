answer = input("expression: ")
x, y, z = answer.split(" ")
if y == "+":
    print(int(x) + int(y))
elif y == "-":
    print(int(x) - int(y))
elif y == "*":
    print(int(x) * int(y))
else y == "/":
    print(int(x) / int(y))