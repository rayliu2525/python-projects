import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("^([1-9]|1[0-2])|(([0-9]|1[0-2]):[0-5][0-9]) (A|P)M to ([1-9]|1[0-2])|(([0-9]|1[0-2]):[0-5][0-9]) (A|P)M$", s):
        beg_time, end_time = s.split(" to ")

        if re.search("^([1-9]|1[0-2]) (A|P)M$", beg_time) and re.search("^([1-9]|1[0-2]) (A|P)M$", end_time):
            l_beg_time, r_beg_time = beg_time.split(" ")
            beg_time = l_beg_time + ":00 " + r_beg_time
            l_end_time, r_end_time = end_time.split(" ")
            end_time = l_end_time + ":00 " + r_end_time

        if "PM" in beg_time and beg_time[0:2] not "12":
            l_time_24, r_time_24 = beg_time.split(":")
            l_time_24 = str(int(l_time_24) + 12)
            beg_time = l_time_24 + ":" + r_time_24

        if "PM" in end_time and end_time[0:2] not "12":
            l_time_24, r_time_24 = end_time.split(":")
            l_time_24 = str(int(l_time_24) + 12)
            end_time = l_time_24 + ":" + r_time_24

        if len(beg_time) == 7:
            beg_time = "0" + beg_time
        if beg_time[0:2] == "12" and "AM" in beg_time:
            beg_time.replace("12", "00", 1)

        if len(end_time) == 7:
            end_time = "0" + end_time
        if end_time[0:2] == "12" and "AM" in end_time:
            end_time.replace("12", "00", 1)


        beg_time = beg_time.replace(" AM", "")
        beg_time = beg_time.replace(" PM", "")

        end_time = end_time.replace(" AM", "")
        end_time = end_time.replace(" PM", "")


        time_range_24 = beg_time + " to " + end_time
        return time_range_24


    else:
        raise ValueError


...


if __name__ == "__main__":
    main()