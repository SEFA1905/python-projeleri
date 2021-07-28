from datetime import datetime
class arackirala(object):
    def __init__(self,aracsayi):
        self.aracsayisi = aracsayi
        self.toplamTutar = 0
        self.hour = 0
        self.minute = 0
        self.hour1 = 0
        self.minute1 = 0
        self.kiralananArac = 0
        self.fiyat=0

    def aracsayisiNe(self):
        print(self.aracsayisi)
    def gunluk(self,nerden,kacArac):
        self.kiralananArac = kacArac
        hour = datetime.now()
        minute = datetime.now()
        self.minute = minute.minute
        self.hour = hour.hour
        self.aracsayisi = self.aracsayisi - kacArac
        if nerden == 'a':
            self.fiyat = 96

        else:
            self.fiyat = 48

    def saatlik(self,nerden,kacArac):
        self.kiralananArac = kacArac
        hour = datetime.now()
        minute = datetime.now()
        self.minute = minute.minute
        self.hour = hour.hour
        self.aracsayisi = self.aracsayisi - kacArac
        if nerden == 'a':
            self.fiyat=6

        else:
            self.fiyat=5

    def aracbirak(self):
        hour = datetime.now()
        minute = datetime.now()
        self.minute1 = minute.minute
        self.hour1 = hour.hour
        son = self.minute - self.minute1
        if son < 0:
            son = son * -1

        self.aracsayisi = self.aracsayisi + self.kiralananArac
        self.toplamTutar = self.kiralananArac * (((self.fiyat / 24) * (self.hour - self.hour1)) + ((self.fiyat / (60 * 24)) * son ))
        return self.toplamTutar
