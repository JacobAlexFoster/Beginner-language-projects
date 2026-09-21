number = int(input("input: "))
while number > 0:
    dig = number % 10
    number = number // 10
    print(dig,end=" ")