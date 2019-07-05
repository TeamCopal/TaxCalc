import tax_logic as tax
import os

os.system("clear")
print("="*10 + " LBHaase ESt-Fix V.01 " + "="*10)
try:
    zvE = float(input("Zu versteuerndes Einkommen: "))
except ValueError:
    zvE = 0.00

using = True
while using:
    os.system("clear")  #Linux
    #os.system("cls")   #Windows
    print("="*10 + " LBHaase ESt-Fix V.01 " + "="*10 + "\n\n Grundlage: {}\n\n\
        1:\t Berechnung der Einkommensteuer\n\
        2:\t Berechnung des Durchschnittsteuersatzes\n\
        3:\t Berechnung des Grenzsteuersatzes\n\
        4:\t Anpassung zvE\n".format(zvE))
    input("Auswahl: ")
