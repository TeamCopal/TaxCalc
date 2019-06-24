import re

def f1(x):
    y = ((x//1) - 9168) / 10000
    return float(re.match(r'\d*.\d{2}', str((y * 980.14 + 1400.0) * y)).group(0))


def f2(x):
    return (216.16 * x + 2397) * x + 965.58


def f3(x):
    return 0.42 * x - 8780.9


def f4(x):
    return 0.45 * x - 16740.68


def tax(x):
    if 9169 <= x <= 14254 :
        return f1(x)
    return 0
