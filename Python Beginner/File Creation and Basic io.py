with open("notes.txt", "w") as file:
    file.write("Hello, this is my first note.\n")
    file.write("Python file handling is simple.\n")
    file.write("End of file.\n")
print("Reading file contents:")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)