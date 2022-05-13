x = input("type a string: ")
lst = []
for char in x:
    if char not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        lst.append(char)
z = "".join(lst)
print(z)

def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()