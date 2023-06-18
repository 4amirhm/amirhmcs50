def convert(str):
    return str.replace(":)" , "🙁").replace(":(" , "🙁")

def main():
    user = input("what did you say? ")
    print(convert(user))

main()
