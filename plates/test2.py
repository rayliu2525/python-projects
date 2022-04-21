s = ["1", "2", "11"]

for x in s:
    if x not in [str(char1) for char1 in range(0,10)]:
        print("yes")