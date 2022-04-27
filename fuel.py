

x, y = input("enter an amount: " ).split(/)
gas_percent = round(x / y * 100)

if x / y * 100 < 1:
    print("E)

elif x > y:


elif x / y * 100 > 99:
    print("F")

else:
    print(gas_percent)


