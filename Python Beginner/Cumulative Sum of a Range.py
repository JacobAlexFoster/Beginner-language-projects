previous_num = 0
for i in range(10):
    x_sum = previous_num + i
    print(f"Current Number {i} Previous Number {previous_num} Sum: {x_sum}")
    previous_num = i