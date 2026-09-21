def func(numlist):
    print("give list:",numlist)
    fnum = numlist[0]
    lnum = numlist[-1]
    if fnum == lnum:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", func(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", func(numbers_y))