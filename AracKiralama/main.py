from classes.Fonksiyonlar import *

while True:
    ana_menu()
    secim = AnaMenuSecim()
    if secim == 'q' or secim == 'Q':
        print("Cikis Yapiliyor...")
        break
    elif secim == 'a' or secim == 'A':
        menu(secim)
    elif secim == 'b' or secim == 'B':
        menu(secim)