import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
            if level > 0:
                break
    except:
        print("Enter a valid number!")

rand_int = random.randint(1, level)

while True:
    guess = input("Guess: ")
    if guess < rand_int:
        print("Too small!")
    elic guess > rand_int:
        print("Too large!")