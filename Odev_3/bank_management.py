'''
Basit Banka Hesap Yönetimi :  Hesap sınıfı oluşturarak bu sınıfa hesap sahibinin 
bilgileri, hesap numarası, bakiye gibi özellikleri ekleyiniz. Ardından para yatırma, para 
çekme, bakiye görüntüleme gibi fonksiyonları gerçekleyiniz. Bu özellikleri kullanarak 
kullanıcıdan bilgileri isteyen ve hesap yönetimini sağlayan Python kodunu yazınız.

'''
#banka hesabi sinifi
class BankaHesabi:

    def __init__(self, hesap_sahibi, hesap_numarasi):

        self.hesap_sahibi = hesap_sahibi
        self.hesap_numarasi = hesap_numarasi
        self.bakiye = 0.0
        
        #islem gecmisini tutmak icin liste 
        self.gecmis = []
            
    def para_yatirma(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"\n{miktar:.2f} TL hesabiniza basariyla yatirildi.")
            print(f"Yeni bakiyeniz:{self.bakiye:.2f} TL")
            
            #islem gecmisine para_yatirma islemini ekleme
            self.gecmis.append(f"{miktar:.2f} TL yatirildi.")
        else:
            print("\nGecersiz miktar, lutfen pozitif bir miktar giriniz!")
    #negatif miktar kabul edilemez      
    def para_cekme(self, miktar):
        if miktar <= 0:
            print("\nGecersiz miktar, lutfen pozitif bir miktar giriniz!")
        #cekilmek istenen miktar bakiyeden buyukse
        elif miktar > self.bakiye:
            print("\nYetersiz bakiye!")
            print(f"Mevcut bakiyeniz: {self.bakiye:.2f} TL")
        else:
            self.bakiye -= miktar
            print(f"\n{miktar:.2f} TL basariyla cekildi.")
            print(f"Kalan bakiyeniz:{self.bakiye:.2f} TL")
            
            #islem gecmisine kaydetme
            self.gecmis.append(f"{miktar:.2f} TL cekildi.")
    #hesap sahibi bilgileri ve bakiye goruntuleme fonksiyonu:       
    def bakiye_goruntuleme(self):
        print("\n--- Hesap Bilgileri ---")
        print(f"Hesap Sahibi:{self.hesap_sahibi}")
        print(f"Hesap Numarasi:{self.hesap_numarasi}")
        print(f"Guncel Bakiye:{self.bakiye:.2f} TL")
        
    #islem gecmisini gostermek icin:
    def gecmis_goster(self):
        print("\n---Islem Gecmisi---")
        if len(self.gecmis) == 0:
            print("Henuz herhangi bir islem yapilmamistir!")
        else:
            for kayit in self.gecmis:
                print("-- " + kayit)

def main():
    print("BANKA HESAP YONETIM SISTEMI")
    
    ad_soyad = input("Hesap sahibinin adi ve soyadini giriniz: ")
    hesap_no = input("Hesap numarasini giriniz: ")
    hesap = BankaHesabi(ad_soyad, hesap_no)
    hesap.bakiye_goruntuleme()
    
    while True:
        #islem secimi icin menu
        print("\n Yapmak Istedgiiniz Islemi Seciniz:")
        print("1-Para Yatirma")
        print("2-Para Cekme")
        print("3-Bakiye Goruntuleme")
        print("4-Islem Gecmisi Goruntuleme")
        print("5-Cıkıs")
        
        secim = input("Islem secimi(1/2/3/4/5): ")
        if secim == '1':
            try:
                miktar = float(input("Yatirmak istediginiz miktar:"))
                hesap.para_yatirma(miktar)
            except ValueError:
                print("\nLutfen gecerli bir miktar giriniz.")
                
        elif secim == '2':
            try:
                miktar = float(input("Cekmek istediğiniz miktar: "))
                hesap.para_cekme(miktar)
            except ValueError:
                print("\nLutfen gecerli bir miktar giriniz.")
                
        elif secim == '3':
            hesap.bakiye_goruntuleme()
            
        elif secim == '4':
            hesap.gecmis_goster()
            
        elif secim == '5':
            print("\nCikis yapiliyor!")
            break
            İ
        else:
            print("\nLutfen isleme devam etmek icin 1-5 arasi bir sayi giriniz.")

if __name__ == "__main__":
    main()
