# import tax_2019_gui_test as taxgui
import tax_logic as lg


def test_wenn_einkommen_kleiner_9168_dann_0():
    assert lg.tax(9000) == 0.00


def test_wenn_einkommen_zwischen_9169_und_14254_dann_f1():
    einkommen = 9169.0
    assert lg.tax(einkommen) == 0.00
    einkommen = 12000.34
    assert lg.tax(einkommen) == 475.00
    
def test_wenn_einkommen_zwischen_14255_und_55960_dann_f2():
    assert lg.tax(40000.53) == 8569.00

def test_wenn_einkommen_zwischen_55961_und_265326_dann_f3():
    assert lg.tax(145323.98) == 52254.00

def test_wenn_einkommen_groesser_265326_dann_f4():
    assert lg.tax(700000.22) == 298259.00