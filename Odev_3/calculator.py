'''
Basit Hesap Makinesi: Kullanıcıdan iki sayı ve bir işlem (+, -, *, /) alarak basit bir hesap 
makinesi programı yazın. Programınız şu işlevleri yerine getirmelidir: kullanıcıdan iki 
sayı ve bir işlem isteme, seçilen işlemi gerçekleştirme, sonucu ekrana yazdırma, sıfıra 
bölme durumunu kontrol etme ve hata mesajı verme, son olarak kullanıcıya başka bir 
işlem yapmak isteyip istemediğini sorma. Program, kullanıcı çıkmak isteyene kadar 
çalışmaya devam etmelidir. 
'''
def hesap_makinesi():
    #kullanicinin hesap makinesinden cikmak isteyene kadar devam edecek ana while dongusu:
    while True:
        #kullanicidan gecerli bir sayi1 alana kadar devam edecek dongu:
        while True:
            print("lutfen ilk sayiyi girin:")
            try:
                sayi1 = float(input())
                break
            except ValueError:
                print("error! lutfen gecerli bir sayi girin!")

        #kullanicidan gecerli bir sayi2 alana kadar devam edecek dongu
        while True:
            print("lutfen ikinci sayiyi girin:")
            try:
                sayi2 = float(input())
                break
            except ValueError:
                print("error! lutfen gecerli bir sayi girin!")

        #islem secimi 
        print("İşlem seçin (+, -, *, /):")
        islem = input()

        #islem "+" ise
        if islem == '+':
            sonuc = sayi1 + sayi2
            print(f"Sonuc: {sayi1} + {sayi2} = {sonuc}")
        #islem "-" ise
        elif islem == '-':
            sonuc = sayi1 - sayi2
            print(f"Sonuc: {sayi1} - {sayi2} = {sonuc}")
        #islem "*" ise
        elif islem == '*':
            sonuc = sayi1 * sayi2
            print(f"Sonuc: {sayi1} * {sayi2} = {sonuc}")
        #islem "/" ise
        elif islem == '/':
            if sayi2 == 0:
                print("error! sifira bolunemez!")
            else:
                sonuc = sayi1 / sayi2
                print(f"Sonuc: {sayi1} / {sayi2} = {sonuc}")

        else:
            print("Gecersiz bir islem girdiniz lutfen '+,-,*,/' seciniz")

        #kullanicinin devam etmek isteyip istemedigini sormak icin yes/no:
        print("\nYeni bir islem ile devam etmek ister misiniz? (y/n):")
        devam = input()

        if devam.lower() != "y":
            print("hesap makinesi islemi bitmistir!")
            break

hesap_makinesi()
