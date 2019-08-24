def gen(x, y):
    while x <= y:
        yield x
        x += 1


g = gen(5, 10)
y = list(g)
print(g)
print(y)
