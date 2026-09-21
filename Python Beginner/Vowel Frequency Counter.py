txt = input("enter an input: ")
vowels = "aeiou"
count = 0
for i in txt.lower():
    if i in vowels:
        count +=1

print(count)