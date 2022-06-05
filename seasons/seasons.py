from datetime import date
import re
import sys
import inflect


def main():
    dob_input = input("Date of Birth: ")
    if re.search("^[1-9]{4}-[1-9]{2}-[1-9]{2}$", dob_input) == None:
        sys.exit("Invaid date")

    year, month, day = dob_input.split("-")

    dob = date(year, month, day)
    current_date = date.today()

    delta = current_date - dob
    minutes = round(delta.total_second() * 60)

    engine_object = inflect.engine()
     = engine_object.number_to_words(minutes)

if __name__ == "__main__":
    main()