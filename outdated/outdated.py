month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)
        if month in list(range(1,13)) and day in list(range(1,32)):
            break
    except:
        try:
            date = input("Date: ")
            old_month, old_day, year = date.split(" ")
            month = month_list.index(old_month) + 1
            day = old_day.replace(",", "")
            day = int(day)
            year = int(year)
            if month in list(range(1,13)) and day in list(range(1,32)):
                break
        except:
            pass

print (f"{year}-{month:02}-{day:02}")
