# vstup od uzivatele, vypise dnesny datum, ak c 1 cervena, 2 zelena, 3 modra "dnes je ... a vybrali jste si barvu...". 
# Ked ine cislo, exit.

from datetime import date
import string
import random

KONSTANTA = 3

def print_message(barva, cislo):
    datum = str(date.today())
    if pravidlo(cislo):
        print("Dnes je " + datum + " a vybrali jste si barvu: " + barva + "!")
    else:
        print("Vybrali jste si barvu: " + barva + "!")

def pravidlo(hodnota):
    return hodnota > KONSTANTA

barvy = ['bila', 'seda', 'cerna']
vstup = int(input('Napiste vstupni hodnotu: '))
if vstup == 1:
    barva = "cervena"
    print_message(barva, vstup)
elif vstup == 2:
    print_message("zelena", 2)
elif vstup == 3:
    print_message("modra", 3)
elif vstup == 4:
    barva = random.choice(barvy)
    print_message(barva)
else:
    print("Vis co Saso? Jdi do prdele.")
    exit()


