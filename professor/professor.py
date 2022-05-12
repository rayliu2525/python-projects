import random


def main():
    question_number = 0
    while True:
        level = get_level()
        if level in [1, 2, 3]:
            break

    while True:
        correct = 0
        question_number += 1
        x = generate_integer(level)
        y = generate_integer(level)
        sum = x + y
        wrong_times = 0
        while True:
            result = input(f"{x} + {y} = ")
            if sum == int(result):
                correct += 1
                break
            else:
                wrong_times += 1
                print("EEE")
                if wrong_times == 3:
                    print(f"{x} + {y} = {sum}")
                    break
        if question_number == 10:
            break

    print(f"score: {correct}")


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
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()