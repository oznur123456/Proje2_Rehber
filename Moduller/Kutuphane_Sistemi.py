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
    print("║  4-Kitap Bilgileri Degistirme  ║")
    print("║  5-Odunc Alma Islemi           ║")
    print("║  6-Guncel Kitap Listesi        ║")
    print("║  7-Cikis                       ║")
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


    elif secim == 4: 
        break 


selamla()
kutuphane_anamenu()