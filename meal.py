def main():
    time_str = input("enter time: ")
    x = convert(time_str)
    if 7 <= x <= 8 :
            print("breakfast time")
    elif 12 <= x <= 13 :
            print("lunch time")
    elif 18 <= x <= 19 :
            print("dinner time")
    else:
            print(" ")
def convert(time_str):
    x1 , x2 = time_str.split(":")
    x1 = int(x1)
    x2 = float(x2)/60
    x = x1 + x2

    return x

if __name__ == "__main__":
    main()