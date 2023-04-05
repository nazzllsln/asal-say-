giris = 0
toplam= 0
print("lütfen bir sayı giriniz, negatif sayılar döngüyü sonlandırır:")
while True:
    giris = int(input("bir sayı giriniz:"))
    if giris<0:
        break #döngüden çıkılıyor "mola"
    toplam+=giris
print("toplam = ", toplam)

