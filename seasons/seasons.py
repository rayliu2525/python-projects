from datetime import date
import re
import sys
import inflect


def main():
    life_minutes(input("Date of Birth: "))

def life_minutes(s):
    if re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", s) == None:
        sys.exit("Invalid date")

    year, month, day = s.split("-")
    year = int(year)
    month = int(month)
    day = int(day)

    dob = date(year, month, day)
    current_date = date.today()

    delta = current_date - dob
    minutes = round(delta.total_seconds() / 60)

    engine_object = inflect.engine()
    minutes_words = engine_object.number_to_words(minutes)

    print(f"{minutes_words} minutes".capitalize().replace(" and", ""))

if __name__ == "__main__":
    main()
    sys.exit(0)