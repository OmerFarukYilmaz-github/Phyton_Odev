class help():
    def __init__(self):
        print("""
                sifrelemeYontemleri sınıfı, içerisinde bazıları simetrik veya asimetrik olmak üzere 13 tane hash metodu içermektedir.
                sifrelemeYontemleri sınıfı ilk çağrıldığında şifrelenmesi istenen text direk kurucu methoda gönderilebilir. 
                Bu durumda istenen metod çağrılırkne texti tekrar göndermeye gerek kalmaz. 
                Veya sınıf nesnesi oluşturulurken değil de istenen metod çağrılırken text gönderilebilir.
                sifrelemeYontemleri sınıfı içerisindeki fonksiyonlar ve detaylı bilgi almak için:
                caesar() => .ceaser
                rot13() => .rot13
                xor() => .xor
                sha() => .sha
                md5() => .md5
                vigeere() => .vigenere
                affine() => .affine
                transposition() => .transposition
                base64() => .base64
                crypto_fernet() => .crypto_fernet
                onetimepad() => .onetimepad
                des() => .des
                res() => .res

        Dil kontrol sınıfının içerisinde metni cümlelerine ayıran cumleayir() fonksiyonu, 
        metni kelimelerine ayıran kelimeayir() fonksiyonu, metin içerisindeki sesli harf sayisini bulan
        sesliharf() fonksiyonu, kelimelerin "Büyük ünlü uyumuna" uyup uymadığını kontrol eden
        uyumKontrol() fonksiyonu ve yapıcı metod olan __init__() fonksiyonu olmak üzere 
        5 farklı fonksiyon bulunmaktadır. 

        dilKontrol sınıfı içerisindeki fonksiyonlar hakkında detaylı bilgi almak için:

        cumleayir() => help.cumleayir()
        kelimeayir() => help.kelimeayir()
        sesliharf() => help.sesliharf()
        uyumKontrol() => help.uyumKontrol()""")

    def cumleayir(self):
        print("""
        cumleayir(self, deger):
        kendisine verilen string degeri cümlelere ayıran ve sayisini geri döndüren fonksiyon
         """)

    def kelimeayir(self):
        print("""
        kelimeayir(self,deger):
        kendisine verilen string degeri kelimelerine ayıran ve sayısını geri döndüren fonksiyon
        """)

    def sesliharf(self):
        print("""

        sesliharf(self,deger):
        kendisine verilen string degerin icerisindeki sesli harf sayisini geri döndüren fonksiyon

        """)

    def uyumKontrol(self):
        print("""
        uyumKontrol(self, deger):

        kendisine verilen string degeri kelimelerine ayırarak kelimelerin tek tek büyük ünlü uyumuna 
        uyup uymadağını bulan ve bunların sayısını döndüren fonksiyon 

        """)

    def ceaser(self):
        print("""
        caesar(text='def', s=4):
        sırasıyla default değerleri 'def' ve 4 olan 2 parametre almaktadır. 
        1. paramatre şifrelenmek üzere gönderilen mesaj
        2. parametre mesaj içerisndeki karakterlerin kaç harf kaydırılacağanı belirtir.
        metod geriye şifrelenmiş metini döndürür.
        """)

    def rot13(self):
        print("""
        rot13(text='def'):
        default değeleri 'def'  olan 1 parametre almaktadır. 
        Bu paramatre şifrelenmek üzere gönderilen mesajı içerir. 
        Bu mesajdaki karakterlerl 13 birim kaydırılaraak şifrelenir.
        Metod geriye şifrelenmiş metini döndürür.
        """)

    def xor(self):
        print("""
              xor(text='def', xor_key='P'):
               sırasıyla default değerleri 'def' ve 'P' olan 2 parametre almaktadır. 
               1. paramatre şifrelenmek üzere gönderilen mesaj
               2. parametre metindeki karakterlerin hangi tek karakterlik key ile xorlanacağını belirtir.
               Metindeki karakterler sırasıyla xor_key ile xor işlemine girer ve metiin şifrelenir.
               Metod geriye şifrelenmiş metini döndürür.
               """)

    def sha(self):
        print("""
              sha(text='def', sha_1=False, sha_224=False, sha_256=False, sha_384=False, sha_512=False):
               sırasıyla default değerleri 'def' ve 'False' olan 2 parametre almaktadır. 
               1. paramatre şifrelenmek üzere gönderilen mesaj
               2. parametre metinin hangi sha metodu ile şifreleneceğini belirtir.
               Metod geriye şifrelenmiş metini döndürür.
               """)

    def md5(self):
        print("""
              md5(text='def'):
              default değeleri 'def' olan 1 parametre almaktadır. 
              Bu paramatre şifrelenmek üzere gönderilen mesajı içerir. 
              Bu mesaj md5 ile şifrelenir.
              Metod geriye şifrelenmiş metini döndürür.
               """)

    def vigenere(self):
        print("""
          vigenere(text='def', key='AYUSH', encode=False, decode=False):
           sırasıyla default değerleri 'def', 'AYUSH' ve 'False' olan 3 parametre almaktadır. 
           1. paramatre işlenmek üzere gönderilen mesaj
           2. parametre metinin hangi key kullanılarak işleneceğini belirtir.
           3. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
           Metod geriye işlenmiş metini döndürür.
           """)

    def affine(self):
        print("""
                  affine(text='def', encode=False, decode=False)
                  sırasıyla default değerleri 'def' ve 'False' olan 2 parametre almaktadır. 
                  1. paramatre işlenmek üzere gönderilen mesaj
                  2. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
                  Metod geriye işlenmiş metini döndürür.
                  """)

    def transposition(self):
        print("""
       transposition(text='def', key=10, encode=False, decode=False):
       sırasıyla default değerleri 'def', '10' ve 'False' olan 3 parametre almaktadır. 
       1. paramatre işlenmek üzere gönderilen mesaj
       2. parametre metinin hangi key kullanılarak işleneceğini belirtir.
       3. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
       Metod keye göre bir matris oluşturp içine metni yazar 
       ve yukarıdan aşağı doğru okuyarak şifreli metni oluşturur.
       Metod geriye işlenmiş metini döndürür.
       """)

    def base64(self):
        print("""
                  base64(text='def', encode=False, decode=False):
                  sırasıyla default değerleri 'def' ve 'False' olan 2 parametre almaktadır. 
                  1. paramatre işlenmek üzere gönderilen mesaj
                  2. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
                  Metod geriye işlenmiş metini döndürür.
                  """)

    def cyrpto_fernet(self):
        print("""
        cyrpto_fernet(text='def', key='', encode=False, decode=False):
        sırasıyla default değerleri 'def', '' ve 'False' olan 3 parametre almaktadır. 
        1. paramatre işlenmek üzere gönderilen mesaj
        2. parametre metinin hangi key kullanılarak işleneceğini belirtir.
        3. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
        Şifreleme yapılacksa key üretilir. şifreleme yapılır. 
        Metod şifreli metni ve daha sonra şifre çözmede kullanılmak üzere keyi dondurur.
        Şifre çözülecekse metin ve key gönderilir. Düz metin döner.  
   """)

    def onetimepad(self):
        print("""
           onetimepad(text='def',key='random' ,encode=False, decode=False):
           sırasıyla default değerleri 'def', 'random' ve 'False' olan 3 parametre almaktadır. 
           1. paramatre işlenmek üzere gönderilen mesaj
           2. parametre metinin hangi key kullanılarak işleneceğini belirtir.
           3. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
           Metod geriye işlenmiş metini döndürür.
           """)

    def des(self):
        print("""        
            des(text='def', encode=False, decode=False):
            sırasıyla default değerleri 'def' ve 'False' olan 2 parametre almaktadır. 
            1. paramatre işlenmek üzere gönderilen mesaj
            2. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
            Metod geriye işlenmiş metini döndürür.
                  """)

    def rsa(self):
        print("""
        rsa(text='def', key='', encode=False, decode=True):
        sırasıyla default değerleri 'def', '' ve 'False' olan 3 parametre almaktadır. 
        1. paramatre işlenmek üzere gönderilen mesaj
        2. parametre metinin hangi key kullanılarak işleneceğini belirtir.
        3. parametre şifreleme içine encode=True olmalı, şifre çözme için decode=True.
        Şifreleme yapılacksa key üretilir. şifreleme yapılır. 
        Metod şifreli metni ve daha sonra şifre çözmede kullanılmak üzere keyi dondurur.
        Şifre çözülecekse metin ve key gönderilir. Düz metin döner.  
   """)