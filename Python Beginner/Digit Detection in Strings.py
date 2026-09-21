input = "Python3"
digpres = False

for char in input:
    if char.isdigit():
        digpres = True
        print("digit detected")
    else:
        print("no digit")

