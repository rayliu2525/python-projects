import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            if level in [1, 2, 3]:
                return level
        except:
            print("type valid number")

def generate_integer(level):
    if level == 1:
        return randint(1, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 999)

if __name__ == "__main__":
    main()