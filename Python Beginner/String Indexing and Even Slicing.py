word = input("input: ")
print("Original String is ", word)
even_chars = word[0::2]

print("Printing only even index chars")
for char in even_chars:
    print(char)