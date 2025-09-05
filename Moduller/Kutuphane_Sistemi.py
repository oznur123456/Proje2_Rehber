
import Kitap_Listesi_Olusturma
import Kitap_Ara
import Kitap_Silme
import Kitap_Bilgileri_Guncelleme
import Kitap_Odunc_Alma
import Guncel_Kitap_Listesi
import Yeni_Kitap_Talep_Listesi

def selamla():
    print("Merhaba! Kutuphane sistemine hos geldiniz.\n")

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
    print("║   Seciminiz nedir?             ║")
    print("╚════════════════════════════════╝")
    print("\033[0m") 

selamla()

while True: 
    kutuphane_anamenu()
    secim = input("Seciminiz icin bir sayi giriniz (1-8): ").strip()

    if not secim.isdigit():
        print("Lutfen bir sayi giriniz.\n")
        continue
        
    secim = int(secim)

    if secim < 1 or secim > 8:
        print("Secim yanlis. 1-8 arasi bir deger giriniz.\n")
        continue

    if secim == 1:
        Kitap_Listesi_Olusturma.kitap_ekle()
    elif secim == 2:
        Kitap_Ara.aranan_kitap()
    elif secim == 3:
        Kitap_Silme.kitap_sil()
    elif secim == 4:
        Kitap_Bilgileri_Guncelleme.kitap_degistir()
    elif secim == 5:
        Kitap_Odunc_Alma.odunc_al()
    elif secim == 6:
        Guncel_Kitap_Listesi.kitaplari_goster()
    elif secim == 7:
        Yeni_Kitap_Talep_Listesi.kitap_talep()
    elif secim == 8:
        print("Programdan cikiliyor.")
        break

selamla()
kutuphane_anamenu()