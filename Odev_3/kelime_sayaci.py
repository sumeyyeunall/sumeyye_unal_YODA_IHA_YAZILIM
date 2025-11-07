'''
Kelime Sayacı: Kullanıcıdan bir cümle veya paragraf alan ve bu metin hakkında çeşitli 
istatistikler hesaplayan bir program yazın. Program şu bilgileri hesaplamalı ve ekrana 
yazdırmalıdır: toplam kelime sayısı, toplam karakter sayısı (boşluklar dahil), en uzun 
kelimenin uzunluğu ve her bir kelimenin kaç kez tekrar ettiği. Bu görev, string 
işlemleri, veri yapıları (örneğin sözlük kullanımı) ve temel algoritma tasarımı 
becerilerinizi test edecektir. Programınızın büyük/küçük harf duyarlılığı konusunda 
nasıl davranacağına karar vermelisiniz ve bu kararınızı kodunuzda açıklamalısınız. 
Ayrıca her satıra ne iş yaptığını açıklayan yorum satırları ekleyin. 
'''
metin=input("bir cumle vya paragraf giriniz:")

#kucuk ve buyuk harflerin ASCII kodlari farkli oldugundan at At AT gibi kelimelerin farkli kelimeler olarak algilanmamasi icin tumunu kucuk harfe cevirmesini saglayan fonks
#s string icin 
def lower_metin(s):
    sonuc = ""
    for ch in s:
        #A ve Z arasindaki harfler+32 ile ASCII kucuk harf karsiligina ceiviriyoruz
        if 'A' <= ch <= 'Z':
            #ord() harflerin ascii kodunu alan fonksiyon
            sonuc += chr(ord(ch) + 32)
        else:
            sonuc += ch
    return sonuc

#hazir len() kullanmadan metin uzunlugunu hesaplamayak icin
def lenght(s):
    count=0
    for _ in s:
        count+=1
    return count
#metni kucuk harfe ceviriyirouz 
metin=lower_metin(metin)

#bosluklar dahil toplam karakteri hesaplama
karakter_sum=lenght(metin)

#kelimeleri tutmak icin liste
kelimeler=[]
#tempicin bos string atamasi
temp="" 
for ch in metin:
    #bosuk gelene kadar her kelimeyi almak icin
    if ch!=" ":
        temp+=ch
    else: 
        #birden fazla bosluk olursa bos ekleme
        if temp!="":
            kelimeler.append(temp)
            temp=""
#dongu sonunda kalanlar varsa
if temp!="":
    kelimeler.append(temp)

#toplam kelime sayisini bulmak icin dongu
kelimeler_sum=0
for _ in kelimeler:
    kelimeler_sum+=1

#en uzun kelimenin uzunlugu 
longest=0
for kelime in kelimeler:
    kelimeUzunlugu=lenght(kelime)
    if kelimeUzunlugu > longest:
            longest=kelimeUzunlugu

#her bir kelimenin kac kez tekrar ettigini bulmak icin
tekrar={}
for kelime in kelimeler: 
    if kelime in tekrar:
        tekrar[kelime]+=1
    else:
        tekrar[kelime]=1

#metnin istatiksel sonuclari
print("\n--- Istatiksel Sonuclar ---")
print("Toplam kelime sayisi:", kelimeler_sum)
print("Toplam karakter sayisi bosluklar ile birlikte:", karakter_sum)
print("En uzun kelimeninin uzunlugu:", longest)
print("\nKelimelerin tekrar sayilari:")
for kelime in tekrar:
    print(kelime, ":", tekrar[kelime])