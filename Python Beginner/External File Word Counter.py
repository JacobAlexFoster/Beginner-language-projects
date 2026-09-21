try:
    with open("sample.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_count = len(words)
        print(f"The file contains {word_count} words.")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")