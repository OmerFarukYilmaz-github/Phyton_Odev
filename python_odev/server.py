from sifreleme import sifrelemeYontemleri
from flask import Flask, jsonify
import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='password',
                     db='voting',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)
app =Flask(__name__)


@app.route('/')
def index():
    return ('server acıldı')


@app.route("/sifrele/sha256/<string:text>", methods=['GET'])
def hash(text):

    if text: # text bos değilse işlem gerçekleniyor
        sifre = sifrelemeYontemleri()

        try:    # sha sifreleme deneniyor
            cipher = sifre.sha(text, sha_256=True)
        except: # sifreleme gercekleşmezse istemciye alttaki mesaj donuyor
            return 'Uzgunum! Sifreleme gerceklestirilemedi'

        baglanti = db.cursor()
        deger = 'avc'
        try:
            sonuc = baglanti.execute('call py_veeri_ekle(%s)', (cipher))
            db.commit()
        except:
            print('hata sifre veritabanına kayıtedilemedi')


        try:    # sifreleme gercekleştiyse şifreli metin donurulmeye calısılıyor
            return jsonify({'cipher_text' : cipher})
        except : # metin gonderilemezse hata mesajı dondurlmeye calısılıyor
            return 'Maalesef sifrelenen mesaj döndürülemedi'

    else:   # text boşsa alltaki mesaj gönderiliyor
        return 'Bos veri gonderilemez',

app.run(host='0.0.0.0',debug=True)

