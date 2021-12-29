import base64
import math
from cryptography.fernet import Fernet
import onetimepad
import pyDes
import rsa
import binascii
import hashlib

class sifrelemeYontemleri:

    def __init__(self, text=''):
        self.text=text
        "bişeyler bişeyler"

    def caesar(self, text='def', s=4):
        if text == 'def':
            text = self.text
        result = ""
        # text'teki karkaterlerl alınınp işleme sokuluyor
        for i in range(len(text)):
            char = text[i]

            if (char.isupper()): # text'teki büyük harfleri şifreliyor
                # ord fonksiyonu ile char'ın int eğeri alınıyor
                # ve sonra alfabede kendinden sonraki (s-1).karaktere kaydırılıyor
                result += chr((ord(char) + s - 65) % 26 + 65)

            else:   # text'teki küçük harfleri şifreliyor
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def rot13(self,text='def'):
        if text == 'def':
            text = self.text

        # ceaser şifrelemeye benziyor fakat 3 değil 13 karakter kaydırıyor
        rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
        return text.translate(rot13trans)

    def xor(self, text='def', xor_key='P'):
        if text == 'def':
            text = self.text
        # Define XOR key
        # Any character value will work
        # calculate length of input string
        length = len(text)

        # perform XOR operation of key
        # with every character in string
        try:
            for i in range(length):
                text = (text[:i] +
                        chr(ord(text[i]) ^ ord(xor_key)) +
                        text[i + 1:])
        except Exception:
            return('bir hata olustu. xor keyin tek haneli oldugundan emin olun')
        return text

    def sha(self, text='def', sha_1=False, sha_224=False, sha_256=False, sha_384=False, sha_512=False):
        if text == 'def':
            text = self.text

        if sha_1:
            cipher_text = hashlib.sha1(text.encode())
        elif sha_224:
            cipher_text = hashlib.sha224(text.encode())
        elif sha_256:
            cipher_text = hashlib.sha256(text.encode())
        elif sha_384:
            cipher_text = hashlib.sha384(text.encode())
        elif sha_512:
            cipher_text = hashlib.sha512(text.encode())

        return cipher_text.hexdigest()

    def md5(self, text='def'):
        if text == 'def':
            text = self.text
        result = hashlib.md5(text.encode())
        return result.hexdigest()

    #buyuk harfle ve bosluksuz yazılan metinlerde calısıyor
    def vigenere(self, text='def', key='AYUSH', encode=False, decode=False):
        if text == 'def':
            text = self.text

        key = list(key)
        if len(text) == len(key):
            ""
        else:
            for i in range(len(text) -
                           len(key)):
                key.append(key[i % len(key)])
        if encode:
            cipher_text = []
            for i in range(len(text)):
                x = (ord(text[i]) +
                     ord(key[i])) % 26
                x += ord('A')
                cipher_text.append(chr(x))
            return ("".join(cipher_text))
        elif decode:
            orig_text = []
            for i in range(len(text)):
                x = (ord(text[i]) -
                     ord(key[i]) + 26) % 26
                x += ord('A')
                orig_text.append(chr(x))
            return ("".join(orig_text))

    def affine(self, text='def', encode=False, decode=False):
        if text == 'def':
            text = self.text
        DIE = 128
        KEY = (7, 3, 55)

        def encryptChar(char):
            K1, K2, kI = KEY
            return chr((K1 * ord(char) + K2) % DIE)

        def decryptChar(char):
            K1, K2, KI = KEY
            return chr(KI * (ord(char) - K2) % DIE)

        if encode:
            return "".join(map(encryptChar, text))
        elif decode:
            return "".join(map(decryptChar, text))

    def transposition(self, text='def', key=10, encode=False, decode=False):
        if text == 'def':
            text = self.text

        if encode:
            ciphertext = [''] * key #sutunlar olusturuluyor

            for col in range(key): # sutun/key sayısı boyunca
                position = col
                while position < len(text):
                    ciphertext[col] += text[position]
                    position += key
            return ''.join(ciphertext)  # Cipher text
        elif decode:
            numOfColumns = math.ceil(len(text) / key)
            numOfRows = key
            numOfShadedBoxes = (numOfColumns * numOfRows) - len(text)
            plaintext = [''] * numOfColumns
            col = 0
            row = 0

            for symbol in text:
                plaintext[col] += symbol
                col += 1
                if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                    col = 0
                    row += 1
            return ''.join(plaintext)

    def base64(self, text='def', encode=False, decode=False):
        if text == 'def':
            text = self.text

        if encode:
            text_bytes = text.encode('ascii')
            try:
                base64_bytes = base64.b64encode(text_bytes)
            except UnicodeEncodeError:
                return 'metin byte cevirileedigi için hata olustu'
            return base64_bytes.decode('ascii')
        elif decode:
            base64_bytes = text.encode('ascii')
            text_bytes = base64.b64decode(base64_bytes)
            return text_bytes.decode('ascii')

    def cyrpto_fernet(self, text='def', key='', encode=False, decode=False):
        if text == 'def':
            text = self.text

        if encode:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            cipher_text = cipher_suite.encrypt( text.encode('ascii'))
            return cipher_text, key
        elif decode:
            cipher_suite = Fernet(key)
            plain_text = cipher_suite.decrypt(text)
            return plain_text.decode('ascii')

    def onetimepad(self, text='def',key='random' ,encode=False, decode=False):
        if text == 'def':
            text = self.text

        if encode:
            cipher = onetimepad.encrypt(text, key)
            return cipher
        elif decode:
            plain = onetimepad.decrypt(text, key)
            return plain

    #simetrik ama textleri b'...' gibi donderiyor bi bak
    def des(self, text='def', encode=False, decode=False):
        if text == 'def':
            text = self.text

        k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

        if encode:
            cipher_text = k.encrypt(text)
            return cipher_text
        elif decode:
            plain_text = k.decrypt(text)
            return plain_text

    #asimetrik
    def rsa(self, text='def', key='', encode=False, decode=True):
        if text == 'def':
            text = self.text

        if encode:
            publicKey, privateKey = rsa.newkeys(512)
            encMessage = rsa.encrypt(text.encode('ascii'),publicKey)
            return encMessage,privateKey
        elif decode:
            decMessage = rsa.decrypt(text, key).decode()
            return decMessage
