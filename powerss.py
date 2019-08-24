from math import floor


def powers(a, n):
    if n == 0:
        return 1
    x = powers(a, floor(n/2))
    if n % 2 == 0:
        return x*x
    else:
        return a*x*x


print(powers(5, 4))
