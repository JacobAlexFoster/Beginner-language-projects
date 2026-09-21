x = int(input("income: "))
if x <= 10000:
    tax = 0
elif x <= 20000:
    tax = (x - 10000)*10/100
else:
    tax = 0 + (10000*10/100)
    tax += (x - 20000)*20/100
print(tax)