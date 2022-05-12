import random


def main():
    ...


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
    if 


if __name__ == "__main__":
    main()