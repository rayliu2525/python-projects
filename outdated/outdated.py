month = [
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
        month, day, year = date.split(/)
        if month in list(range(1,13)) and day in list(range(1,32)):
            break
    except:
        try:
            date = input("Date: ")
            old_month, old_day, year = date.split(" ")
        except:
            pass
print
