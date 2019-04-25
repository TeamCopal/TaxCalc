def f1(x):
    y = 10**4
    return (980.14 * (x/y) + 1400) * (x/y)


def f2(x):
    return (216.16 * x + 2397) * x + 965.58


def f3(x):
    return 0.42 * x - 8780.9


def f4(x):
    return 0.45 * x - 16740.68


def tax(x):
    if x == 9169:
        return f1(9169)
    return 0


print(f1(10))
