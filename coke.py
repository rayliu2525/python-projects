x = 0
while x < 50:
    y = int(input("enter a value: "))
    if y in [5, 10, 25]:
        x = x + y
        print(f"{50 - x} is due")
    print(f"{50-x} is due")
print(x -50)