num = int(input("input number: "))
str_num = str(num)
rev_str = str_num[::-1]
if str_num == rev_str:
    print("palindrome")
else:
    print("not palindrome")