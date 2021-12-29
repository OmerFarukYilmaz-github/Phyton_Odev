from  sifreleme import sifrelemeYontemleri
from yazim_kurallari import kontrol
from help import help



text="İlk yarıyı yenik kapatan Adana ekibi, ikinci yarıda istediğini aldı ve sahadan 3-2 galip ayrılarak tur atladı."
print("cümle sayisi: ",kontrol.cumleayir(text))
print("kelime sayisi: ",kontrol.kelimeayir(text))
print("sesli harf sayisi: ",kontrol.sesliharf(text))
print("büyük ünlü uyumuna uyan/ uymayan kelime sayisi: ",kontrol.uyumKontrol(text))

print()
sifre=sifrelemeYontemleri('')
text = "CEASER CIPHER DEMO"
s = 4
print(text)
print("Ceaser sifreli: " + sifre.caesar(text, s))
print()

txt = "ROT13 Algorithm"
print(text)
print("Rot13 sifreli: ",sifre.rot13(txt))
print()

text='Xor'
print(text)
c=sifre.xor(text)
print("xor sifreli: ",c)
p=sifre.xor(c)
print('xor cozulmus: ',p)
print()


text='Sha 256 Encrypt'
print(text)
c=sifre.sha(text, sha_256=True)
print("sha 256 Encrypted:", c)
print()


text='OmerFaruk'
print(text)
c=sifre.md5(text)
print("md 5 Encrypted:", c)
print()

text='sELAMLAr'
print(text)
c=sifre.vigenere(text.upper(),encode=True)
print("vigenere sifreli: ",c)
p=sifre.vigenere(c, decode=True)
print('vigenere cozulmus: ',p)
print()

text='affine deneme'
print(text)
c=sifre.affine(text,encode=True)
print("affine sifreli: ",c)
p=sifre.affine(c, decode=True)
print('affine cozulmus: ',p)
print()


text='Transposition Cipher'
print(text)
c=sifre.transposition(text, key=10, encode=True)
print("transposition sifreli: ",c)
p=sifre.transposition(c, key=10, decode=True)
print('transposition cozulmus: ',p)
print()

text="Python is fun"
print(text)
c_text=sifre.base64(text, encode=True)
print('sifreil ',c_text)
p=sifre.base64(c_text, decode=True)
print('cozulmus', p)
print()


text="This example is used to demonstrate cryptography module"
print(text)
cipher_text,key= sifre.cyrpto_fernet(text,encode=True)
print('fernet sifreli hali', cipher_text)
print('fernet cozumlenmıs hali', sifre.cyrpto_fernet(cipher_text,key= key, decode=True))
print()


text='One Time Cipher'
print(text)
c=sifre.onetimepad(text, key='abi', encode=True)
print('onetimepad sifreli: ',c)
p=sifre.onetimepad(c, key='abi', decode=True)
print('onetimepad cozulmus: ',p)
print()


text = 'DES Algorithm Implementation'
print(text)
c = sifre.des(text, encode=True)
print('des sifreli: ', c)
p = sifre.des(c, decode=True)
print('des cozulmus: ', p)
print()


text='Bu bir deneme'
print(text)
c,key=sifre.rsa(text, encode=True)
print("rsa Encrypted:", c)
p=sifre.rsa(c, key=key, decode=True)
print('rsa Decrypted:', p)
print()

