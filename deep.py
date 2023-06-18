# gets the input from user
x = input("what did  just say? ").lower().strip()

# gives answare to user
if x == "42":
         print("yes")
elif x == "forty-two":
         print("yes")
elif x == "forty two":
         print("yes")
else:
         print("No")