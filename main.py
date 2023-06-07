import sqlite3

# Veritabanı dosyasının yolu
veritabani_yolu = "C:\\Kullanıcılar\\<kullanici_adi>\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

# Veritabanına bağlanma
baglanti = sqlite3.connect(veritabani_yolu)
cursor = baglanti.cursor()

# Veritabanından verileri sorgula
cursor.execute("SELECT * FROM urls")

# Sonuçları al ve metin dosyasına kaydet
with open("chrome_verileri.txt", "w", encoding="utf-8") as dosya:
    for satir in cursor.fetchall():
        dosya.write(str(satir) + "\n")

# Bağlantıyı kapat
cursor.close()
baglanti.close()

print("Chrome verileri başarıyla kaydedildi.")

#Python'da Google Chrome'un verilerine erişmek ve bunları bir metin dosyasına kaydetmek için sqlite3 modülünü kullanabiliriz. Google Chrome, kullanıcı verilerini SQLite veritabanı dosyalarında depolar. İşte bu veritabanlarına erişerek verileri metin dosyasına kaydetmenin bir örneği Yukarıdaki örnek kodda, Chrome'un "History" veritabanına bağlanarak urls tablosundaki verileri sorguluyoruz. Sonuçları bir metin dosyasına (chrome_verileri.txt) yazıyoruz. veritabani_yolu değişkenini kendi kullanıcı adınıza ve işletim sistemine göre güncellemeniz gerektiğini unutmayın.

#Bu kodu çalıştırdığınızda, Chrome'un geçmişindeki URL'leri ve ilgili bilgileri içeren bir metin dosyası oluşturulacaktır. Ancak, unutmayın ki Chrome'un veritabanı yapısı zamanla değişebilir ve bu kod güncel sürümlerde çalışmayabilir.
