def main():
    x = input("What time is it?: ")
    conv_time = convert(x)
    if 7 <= conv_time <= 8:
        print("breakfast time")
    elif 12 <= conv_time <= 13:
        print("lunch time")
    elif 18 <= conv_time <= 19:
        print("dinner time")

def convert(time):
    x, y = time.split(":")
    y = int(y)/60
    return x + y


if __name__ == "__main__":
    main()