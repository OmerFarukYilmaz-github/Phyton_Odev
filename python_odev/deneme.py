"""
sifre = sifrelemeYontemleri()
text="Python is fun"
c_text=sifre.base64(text, encode=True)
print('sifreil ',c_text)
print('cozulmus', sifre.base64(c_text, decode=True))
"""




"""
sifre = sifrelemeYontemleri()
text='GeeksforGeeks'
c=sifre.md5(text)
print("Encrypted:", c)
"""
"""
text="This example is used to demonstrate cryptography module"
cipher_text,key= sifre.cyrpto_fernet(text,encode=True)
print('sifreli hali', cipher_text)
print('cozumlenmıs hali', sifre.cyrpto_fernet(cipher_text,key= key, decode=True))
"""
""" check the above function
text = "CEASER CIPHER DEMO"
s = 4
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + yontem1.Caesar_encrypt(text, s))
"""
"""
txt = "ROT13 Algorithm"
print(sifre.rot13_encrypt(txt))
"""
"""
print(
sifre.transposition_encrypt('3214', 'HELLO')
)"""
"""
print(
sifre.transposition_encrypt(6, 'Transposition Cipher')
)
print(
sifre.transposition_decrypt(6,sifre.transposition_encrypt(6, 'Transposition Cipher'))
)"""
"""
text="Python is fun"
c_text=sifre.base64_encode(text)
print('sifreil ',c_text)
print('cozulmus', sifre.base64_decode(c_text))
"""
"""
text='One Time Cipher'
c=sifre.onetimepad(text, key='abi' ,encode=True)
print('sifreli: ',c)
p=sifre.onetimepad(c, key='abi',decode=True)
print('cozulmus: ',p)
"""
"""
sifre = sifrelemeYontemleri()
text = 'DES Algorithm Implementation'
c = sifre.des(text, encode=True)
print('sifreli: ', c)
p = sifre.des(c, decode=True)
print('cozulmus: ', p)
"""
"""
sifre = sifrelemeYontemleri()
text='Bu bir deneme'
c,key=sifre.rsa(text, encode=True)
print("Encrypted:", c)
p=sifre.rsa(c, key=key, decode=True)
print('Decrypted:', p)
"""
"""sifre = sifrelemeYontemleri()
text='GeeksforGeeks'
c=sifre.sha(text, sha_256=True)
print("Encrypted:", c)
"""
"""sifre = sifrelemeYontemleri()
text='GeeksforGeeks'
c=sifre.md5(text)
print("Encrypted:", c)"""

"""sifre = sifrelemeYontemleri()
text='Transposition Cipher'
c=sifre.transposition(text, key=10, encode=True)
print("sifreli: ",c)
p=sifre.transposition(c, key=10, decode=True)
print('cozulmus: ',p)"""

"""sifre = sifrelemeYontemleri()
text='GeeksforGeeks'
c=sifre.xor(text)
print("sifreli: ",c)
p=sifre.xor(c)
print('cozulmus: ',p)
"""
"""sifre = sifrelemeYontemleri()

text='sELAMLAr'
c,key=sifre.vigenere(text.upper(),encode=True)
print("sifreli: ",c)
p=sifre.vigenere(c,key, decode=True)
print('cozulmus: ',p)
"""