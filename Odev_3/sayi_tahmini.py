'''
Sayı Tahmini: Bir sayı tahmin oyunu programı yazın. Program, 1 ile 100 arasında 
rastgele bir sayı seçmeli ve kullanıcıdan bu sayıyı tahmin etmesini istemelidir. Kullanıcı 
her tahmin yaptığında, program tahminin doğru sayıdan yüksek mi yoksa düşük mü 
olduğunu söylemelidir. Kullanıcıya 10 tahmin hakkı verin. Kullanıcı doğru tahmin 
ettiğinde veya tahmin hakkı bittiğinde oyun sona ermelidir. Program, kullanıcının kaç 
denemede doğru tahmin ettiğini veya tahmin hakkının bittiğini bildirmelidir. Ayrıca 
her satıra ne iş yaptığını açıklayan yorum satırları ekleyin.

'''
import random

def sayi_tahmin_oyunu():
    
    #1-100 arasi rastgele bir sayi seciyoruz:
    rastgele_sayi = random.randint(1, 100)
    
    #kullanici tahmin hakki:
    tahmin_hakki = 10
    
    #kullanicinin denemelerini saymak icin sayac:
    deneme_sayisi = 0

    print("Sayi Tahmin Oyunu!")
    print(f"1 ile 100 arasinda bir sayi tahmin etmeniz gerekiyor ve {tahmin_hakki} hakkiniz var!")

    #deneme sayisi tahmin hakkindan kucuk oldugu surece tahmin dongusu devam eder:
    while deneme_sayisi < tahmin_hakki:
        
        #kullaniciya kalan tahmin hakkini gostermek icin:
        kalan_hak = tahmin_hakki - deneme_sayisi
        tahmin_str = input(f"Tahmininiz (Kalan Hak: {kalan_hak}): ")

        #sayi yerine harf vs girilmemesi icin hata yonetimi girdi integer degilse error:
        try:
            #integer kontrolu
            kullanici_tahmini = int(tahmin_str)
        except ValueError:
            #integer degilse
            print("Lutfen 1-100 arasi bir sayi giriniz!")
            #error durumunda tahmin hakki bu sekilde eksilmemis olur
            continue 

        #integer girildiginde deneme_sayisi sayacini 'ni artiriyoruz
        deneme_sayisi += 1

        #tahminin rastgele_sayi olup olmadigiyla ilgili kontrol:
        if kullanici_tahmini == rastgele_sayi:
            #dogru tahmin ettiginde oyun sona erer ve kacinci denemede dogru tahmin ettigini kullaniciya bildiriyoruz:
            print(f"{rastgele_sayi} sayisini {deneme_sayisi}. denemenizde dogru tahmin ettiniz!")
            break

        elif kullanici_tahmini < rastgele_sayi:
            #tahminimiz rastgele_sayi dan dusukse
            print("Daha YUKSEK bir sayi girmelisiniz.")
            
        else: 
            #tahminimiz rastgele_sayi dan yuksekse
            print("Daha DUSUK bir sayi girmelisiniz.")

    #tahmin hakki bittigi icin dongu sonlandiginda kullaniciya bunu bildirmek icin:
    if deneme_sayisi == tahmin_hakki and kullanici_tahmini != rastgele_sayi:
        print(f"Tahmin hakkiniz bitti! Dogru tahmin {rastgele_sayi}")

if __name__ == "__main__":
    sayi_tahmin_oyunu()