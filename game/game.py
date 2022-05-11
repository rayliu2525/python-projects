import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
            if level > 0:
                break
    except:

rand_int = random.randint(1, level)
guess = input("Guess: ")