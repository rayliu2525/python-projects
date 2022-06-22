import sys

def main():
    try:
        starting_balance = input("How much money is in your bank account? ")
        starting_balance = convert(starting_balance)
    except:
        sys.exit("Not a valid number")

    interest_rate = input("What interest rate do you expect? ")
    length = input("How many years will your account accrue the aforementioned interest rate? ")

def convert(x):
    return int(x)
