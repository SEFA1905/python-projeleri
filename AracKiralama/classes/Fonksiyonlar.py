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
def MenuSecim():
    pass