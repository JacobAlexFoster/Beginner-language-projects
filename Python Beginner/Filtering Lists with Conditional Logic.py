num_list = [10, 20, 33, 46, 55]
new = []

for i in range(len(num_list)):
    if num_list[i] % 5 == 0:
        new.append(num_list[i])

print(new)
