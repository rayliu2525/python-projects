def main():
    ...


def shorten(word):
    lst = []
    for char in word:
        if char not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            lst.append(char)
    new_word = "".join(lst)
    print(z)


if __name__ == "__main__":
    main()