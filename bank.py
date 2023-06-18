#user greeting

user_greeting = input(": ").strip().lower()

if "hello" in user_greeting :
    print("$0")
elif "h" == user_greeting[0]:
    print("$20")
else:
     print("$100")
