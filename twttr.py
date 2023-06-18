str = input("x :")
vowel = ["a","A","e","E","i","I","o","O","u","U"]
for word in vowel:
      str = str.replace(word, "")
print(str)