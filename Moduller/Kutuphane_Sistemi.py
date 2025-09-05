import Kitap_Listesi_Olusturma
import Kitap_Ara
import Kitap_Silme
import Kitap_Bilgileri_Guncelleme
import Kitap_Odunc_Alma
import Guncel_Kitap_Listesi
import Yeni_Kitap_Talep_Listesi

def selamla():
    print("Merhaba! Kutuphane sistemine hos geldiniz.")
    
def kutuphane_anamenu():
    print("\033[1;35;40m")
    print("╔════════════════════════════════╗")
    print("║\033[1;33;40m        KUTUPHANE SISTEMI     \033[1;35;40m  ║")
    print("║                                ║")
    print("║  1-Kitap Ekle                  ║")
    print("║  2-Kitap Ara                   ║")
    print("║  3-Kitap Silme                 ║")
    print("║  4-Kitap Bilgileri Guncelleme  ║")
    print("║  5-Odunc Alma Islemi           ║")
    print("║  6-Guncel Kitap Listesi        ║")
    print("║  7-Yeni Kitap Talebi           ║")
    print("║  8-Cikis                       ║")
    print("║                                ║")
    print("║   Seçiminiz nedir?             ║")
    print("╚════════════════════════════════╝")
    print("\033[0m") 
    
selamla()

while True: 
    kutuphane_anamenu()
    secim = (input("Seçiminiz icin bir sayi giriniz (1-6): "))

    if not secim.isdigit():
        print("Lütfen bir sayi giriniz.")
        continue
        
    secim = int(secim)

    if secim < 1 or secim > 6:
        print("Secim yanlis. 1-6 arasi bir deger giriniz.")
        continue

    if secim == 1: 
        import Kitap_Listesi_Olusturma 
        Kitap_Listesi_Olusturma.kitap_ekle()

    if secim == 2: 
        import Kitap_Ara 
        Kitap_Ara.aranan_kitap()

    if secim == 3: 
        import Kitap_Silme 
        Kitap_Silme.kitap_sil()

    if secim == 4: 
        import Kitap_Bilgileri_Guncelleme 
        Kitap_Bilgileri_Guncelleme.kitap_degistir()

    if secim == 5: 
        import Kitap_Odunc_Alma
        Kitap_Odunc_Alma.odunc_al()

    if secim == 6: 
        import Guncel_Kitap_Listesi 
        Guncel_Kitap_Listesi.kitaplari_goster()

    if secim == 7: 
        import Yeni_Kitap_Talep_Listesi
        Yeni_Kitap_Talep_Listesi.kitap_talep()

    if secim == 8: 
        print ("Kutuphane sisteminden cikiliyor.")
        break

selamla()
kutuphane_anamenu()