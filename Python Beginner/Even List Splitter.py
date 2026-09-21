numbers = [12,7,34,21,5,10,8,3,19,2]

evens = []
odds = []

for n in numbers:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(evens)
print(odds)
