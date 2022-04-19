def convert(param1):
    x = param1.replace(":)", "🙂").replace(":(", "🙁")
    return x


y = input("write your sentence: ")
z = convert(y)
print(z)