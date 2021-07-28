from classes.Fonksiyonlar import *
from classes.araba import araba
from classes.bisiklet import bisiklet

ana_menu()
secim = AnaMenuSecim()
while True:

    if secim == 'q' or secim == 'Q':
        print("Cikis Yapiliyor...")
        break
    elif secim == 'a' or secim == 'A':
        menu(secim)
        secim1 = MenuSecimAraba()
        if secim1 == '5':
            print("Cikis Yapiliyor...")
            break
        secimler('a',secim1,a1)


    elif secim == 'b' or secim == 'B':
        menu(secim)
        secim1 = MenuSecimBisiklet()

        if secim1 == '5':
            print("Cikis Yapiliyor...")
            break
        secimler('b',secim1,b1)

