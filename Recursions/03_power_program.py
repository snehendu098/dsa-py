def power(b, p):
    if (p == 1):
        return b
    if (p != 1):
        return (power(b, (p-1)) * b)


print(power(2, 3))
