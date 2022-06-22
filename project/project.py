import sys

def main():
    try:
        starting_balance = input("How much money is in your bank account? ")
        starting_balance = convert(starting_balance)
    except:
        sys.exit("Not a valid answer")
    try:
        interest_rate = input("What interest rate do you expect? ")
        interest_rate = convert(interest_rate)
    except:
        sys.exit("Not a valid answer")
    try:
        length = input("How many years will your account accrue the aforementioned interest rate? ")
        length = convert(length)
    except:
        sys.exit("Not a vlid answer")



def convert(x):
    return int(x)

def end_balance()