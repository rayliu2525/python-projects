def convert(param1):
    x = param1.replace(":)", "🙂").replace(":(", "🙁")
    return x

def main():
    y = input("write your sentence: ")
    z = convert(y)
    print(z)

main()
