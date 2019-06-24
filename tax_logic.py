import re

def f1(x):
    y = ((x//1) - 9168) / 10**4
    return (y * 980.14 + 1400.00) * y


def f2(x):
    z = ((x//1) - 14254) / 10**4
    return (216.16 * z + 2397.00) * z + 965.58


def f3(x):
    return 0.42 * (x//1) - 8780.9


def f4(x):
    return 0.45 * (x//1) - 16740.68


def tax(x):
    ''' Ermittelt zu zahlende ESt anhand von ESt-Klassen

    Args:
        x (int): zvE (zu versteuerndes Einkommen)

    Returns:
        payrate (int): zu zahlende Einkommensteuer
    '''
    payrate = 0.00

    # ESt-Klasse 1
    if 9169.00 <= x <= 14254.00 :
        payrate = f1(x)

    # ESt-Klasse 2
    if 14255.00 <= x <= 55960.00 :
        payrate = f2(x)

    # ESt-Klasse 3
    if 55961.00 <= x <= 265326.00 :
        payrate = f3(x)

    # ESt-Klasse 4
    if x > 265326.00 :
        payrate = f4(x)

    # "Runden" zu Vorteil des Steuerzahlers
    if payrate > 0:
        return float(payrate//1)
    return payrate
