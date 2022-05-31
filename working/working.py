import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("^([1-9]|1[0-2])|([0-9]|1[0-2]):[0-5][0-9]) (A|P:M) to ([1-9]|1[0-2])|([0-9]|1[0-2]):[0-5][0-9]) (A|P)M$", s):
        beg_time, end_time = s.split(" to ")
        if re.search("^([1-9]|1[0-2]): (A|P)M)$", beg_time) and re.search("^([1-9]|1[0-2]): (A|P)M)$", end_time):
            l_beg_time, r_beg_time = beg_time.split(" ")
            beg_time = l_beg_time + ":00 " + r_beg_time
            l_end_time, r_end_time = end_time.split(" ")
            end_time = l_end_time + ":00 " + r_end_time"

        if PM in beg_time
            l_time_24, r_time_24 = beg_time.split(":")
            l_time_24 = str(int(l_time_24) + 12)
            beg_time_24 = l_time_24 + ":" + r_time_24

        if PM in end_time
            l_time_24, r_time_24 = end_time.split(":")
            l_time_24 = str(int(l_time_24) + 12)
            end_time_24 = l_time_24 + ":" + r_time_24


    else:
        raise ValueError


...


if __name__ == "__main__":
    main()