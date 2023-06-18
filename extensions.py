# user input
x = input("please enter media type: ").strip().lower()
x = x.split(".")[-1]
x = x.replace(".","")

# condition
if "gif" in x :
    print("image/gif")
elif "jpg" in x:
    print("image/jpeg")
elif "png" in x:
    print("image/png")
elif "pdf" in x:
    print("application/pdf")
elif "txt" in x:
    print("text/plain")
elif "zip" in x :
    print("application/zip")
elif "jpeg" in x:
    print("image/jpeg")
else:
   print("application/octet-stream")