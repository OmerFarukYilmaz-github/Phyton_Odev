import re

class dilKontrol:
    def __init__(self, kalinunluler, unluler, inceunluler):
        self.kalinunluler = kalinunluler
        self.unluler = unluler
        self.inceunluler = inceunluler

    def cumleayir(self, deger):
        ayrikcumle = re.split(r'[.!?]+', deger)
        return len(ayrikcumle) - 1

    def kelimeayir(self, deger):
        ayrikkelime = deger.split(" ")
        return len(ayrikkelime)

    def sesliharf(self, deger):
        deger = deger.lower()
        count = 0
        for i in deger:
            for vowel in self.unluler:
                if i == vowel:
                    count += 1

        return count

    def uyumKontrol(self, deger):
        uyan = 0
        uymayan = 0
        deger = deger.split(" ")
        for kelime in deger:

            if (((sum(kelime.count(ince) for ince in self.inceunluler)) != 0) and (sum(kelime.count(kalin) for kalin in
                                                                                       self.kalinunluler)) != 0):  # Aynı kelime içerisinde hem kalın ünlü hem de ince ünlü bulunuyor mu diye bakar.

                uymayan += 1
            else:

                uyan += 1
        return uyan, uymayan

"""
str = ""bilezik. ceylan. gazete.""

unluler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
kalin_unluler = ['a', 'ı', 'o', 'u']
ince_unluler = ['e', 'i', 'ö', 'ü']

kontrol = dilKontrol(kalin_unluler, unluler, ince_unluler)

help = help()

print("cümle sayisi: ", kontrol.cumleayir(str))

print("kelime sayisi: ", kontrol.kelimeayir(str))

print("sesli harf sayisi: ", kontrol.sesliharf(str))

print("(büyük ünlü uyumuna uyan, büyük ünlü uyumuna uymayan): ", kontrol.uyumKontrol(str))

"""

