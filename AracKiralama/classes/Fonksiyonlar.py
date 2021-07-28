from classes.araba import araba
from classes.bisiklet import bisiklet


a1 = araba(10)
b1 = bisiklet(5)

def ana_menu():
    print("""
    ******** Arac Kirala ********
            A-Araba
            B-Bisiklet
            Q-Cikis 
    """)
def AnaMenuSecim():
    while True:
        try:
            secim = input("Ne Tur Araba Kiralayacaksınız:")
            if (secim == 'a') or (secim == 'A') or (secim == 'b') or (secim == 'B') or (secim == 'q') or (secim == 'Q'):
                return secim
                break
            else:
                print("Lutfen 'A','B','Q' den Birini Seciniz")
        except ValueError:
                print("Lutfen Geçerli Bir Secim Yapınız")
def menu(secim):
    if (secim == 'a') or (secim == 'A'):
        print("""
        *****************************************               
        Arabanın Gunluk Kiralama Fiyati 96 TL dir
        Arabanın Saatlik Kiralama Fiyati 6TL dir     
        *****************************************
                        """)
    else:
        print("""
        *******************************************            
        Bisikletin Gunluk Kiralama Fiyati 48 TL dir
        Bisikletin Saatlik Kiralama Fiyati 5TL dir 
        *******************************************
                            """)
def MenuSecimAraba():
    while True:
        try:
            secim = input("""
    1-Arabayi Gunluguk Kirala
    2-Arabayi Saatlik Kirala
    3-Kac Araba Var
    4-Arabaları Geri Ver
    5-Cikis
    Seciminizi Yapiniz:""")
            if (secim == '1') or (secim == '2') or (secim == '3') or (secim == '4') or (secim == '5'):
                return secim
                break
            else:
                print("Gecerli Bir Secim Yapiniz")
        except ValueError:
            print("Lutfen Geçerli Bir Secim Yapınız")
def MenuSecimBisiklet():
    while True:
        try:
            secim = input("""
    1-Bisikleti Gunluguk Kirala
    2-Bisikleti Saatlik Kirala
    3-Kac Bisiklet Var
    4-Bisikletleri Geri Ver
    5-Cikis
    Seciminizi Yapiniz:""")
            if (secim == '1') or (secim == '2') or (secim == '3') or (secim == '4') or (secim == '5'):
                return secim
                break
            else:
                print("Gecerli Bir Secim Yapiniz")
        except ValueError:
            print("Lutfen Geçerli Bir Secim Yapınız")

def secimler(nerden,secim,ne):
    if secim == '1':
        kacTane = kacArac()
        ne.gunluk(nerden,kacTane)
    if secim == '2':
        kacTane = kacArac()
        ne.saatlik(nerden,kacTane)
    if secim == '3':
        ne.aracsayisiNe()
    if secim == '4':
       print(ne.aracbirak())


def kacArac():
    return int(input("Kac Arac Kiralanacak"))
