s = "5"

for char in s:
    if char not in [str(char1) for char1 in range(0,10)]:
        print("hello")
pass