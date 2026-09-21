x = int(input("input: "))
str_num = str(x)
if str_num == str_num[::-1]:
    print("is palindrome")
else:
    print("isnt palindrome")