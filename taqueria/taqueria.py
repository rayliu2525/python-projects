total = 0

while True:

    try:
        item = input("Enter Item: ").lower().title()
    except EOFError:
        quit()

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    if item in menu:
        total += menu[item]
        format_float = "{:.2f}".format(total)
        print(f"${format_float}")

