x, y, z = input("entet your values: ").split(" ")
x = float(x)
z = float(z)

if y == "+" :
    res = x + z
elif y == "*" :
    res = x * z
elif y == "/" :
    res = x / z
elif y == "-" :
    res = x - z

print("{:.1f}".format(res))