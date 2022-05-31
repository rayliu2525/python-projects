import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("^([1-9]|1[0-2])|([0-9]|1[0-2]):[0-5][0-9]) (A|P:M) to ([1-9]|1[0-2])|([0-9]|1[0-2]):[0-5][0-9]) (A|P)M$", s):
        beg_time, end_time = s.split(" to ")
        if re.search("^([1-9]|1[0-2]): (A|P)M)$", beg_time) and re.search("^([1-9]|1[0-2]): (A|P)M)$", end_time):
            beg_time.split()
            end_time = f"{end_time}:00"
        if beg_time.split(":")[0]


    else:
        raise ValueError


...


if __name__ == "__main__":
    main()