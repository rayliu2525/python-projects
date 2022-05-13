def main(word):
    no_vowel = shorten(word)
    print(no_vowel)

def shorten(word):
    lst = []
    for char in word:
        if char not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            lst.append(char)
    new_word = "".join(lst)
    return new_word


if __name__ == "__main__":
    main("hello My Name is Raymond")