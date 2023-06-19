# dic of fruits
fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantalop" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 50,
    "strawberries" : 50,
    "tangerine" : 100,
    "watermelon" : 80,
    "sweet cherries" : 100
}

# gets the ser input
user_input = input("what fruit? ").lower()

# gives the calori
if user_input in fruits:
    print("Calories: ", fruits[user_input])