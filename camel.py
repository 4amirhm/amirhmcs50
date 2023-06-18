def main():
    snake_case()

def snake_case():
    n = input("camel case: ")
    for i in n:
        if i.isupper():
            print("_"+ i.lower(), end="")
        else:
            print(i, end="")

main()
print()