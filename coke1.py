# sets the amount that user has to pay ith the exact coins
amount_due = 0
coin = [5, 10, 25]

# it runs the program until the amont is right
while (1):
    user_coin = int(input("insert coin: "))
    amount_due += user_coin
    if user_coin not in coin:
        if amount_due < 50:
            print(f"Amount Due: {50}" )
        elif amount_due >= 50:
            print(f"Change Owed: {amount_due - 50}" )
            break
    elif user_coin in coin:
        if amount_due < 50:
            print(f"Amount Due: {50 - amount_due}" )
        elif amount_due >= 50:
            print(f"Change Owed: {amount_due - 50}" )
            break
