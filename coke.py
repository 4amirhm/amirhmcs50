amount_due = 50
coin = [5, 10, 25]

# it runs the program until the amont is right
while amount_due > 0:
    print(f"Amount Due: {amount_due}" )
    user_coin = int(input("insert coin: "))
    if user_coin in coin:
        amount_due -= user_coin

# if user payes more, it charges the account
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")