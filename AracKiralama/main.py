from classes import deneme


print("""
******** Arac Kirala ********
        A-Araba
        B-Bisiklet
        Q-Cikis 
""")
while True:
    try:
        secim=input("Ne Tur Araba Kiralayacaksınız:")
        if (secim=='a')or (secim=='A')or (secim=='b')or (secim=='B')or (secim=='q')or (secim=='Q'):
            break
        else:
            print("Lutfen 'A','B','Q' den Birini Seciniz")
    except ValueError:
        print("Lutfen Geçerli Bir Secim Yapınız")