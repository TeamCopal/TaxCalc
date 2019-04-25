# import tax_2019_gui_test as taxgui
import tax_logic as lg


def test_wenn_einkommen_kleiner_9168_dann_0():
    assert lg.tax(9000) == 0


def test_wenn_einkommen_groessergleich_9169_dann_f1():
    einkommen = 9169
    assert lg.tax(einkommen) == lg.f1(einkommen)
