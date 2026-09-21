def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(result)
a = int(input("input base: "))
b = int(input("input exponent: "))
exponent(a, b)