def selamla():
    print("Merhaba!")
    


while True: 
    def kutuphane_anamenu():

        print("\033[1;35;40m")
        print("╔═════════════════════════════════╗")
        print("║\033[1;33;40m     KUTUPHANE SISTEMI    \033[1;35;40m  ║")
        print("║                                 ║")
        print("║  1-Kitap Ekle                   ║")
        print("║  2-Kitap Ara                    ║")
        print("║  3-Tum Kitaplari Listele        ║")
        print("║  4-Odunc Alma Islemi            ║")
        print("║  5-Ogrenci Kitap Okuma Verisi   ║")
        print("║  6-Cikis                        ║")
        print("║                                 ║")
        print("║   Seçiminiz nedir?              ║")
        print("╚═════════════════════════════════╝")
        print("\033[0m") 

    secim = int(input("Seçiminiz icin bir sayi giriniz (1-6): "))


    if secim.isalpha or secim < 1 or secim > 6:
        print("Secim yanlis. 1-6 arasi bir deger giriniz.")
        continue

    if secim == "1": 
        print ("Lutfen eklemek istediginiz kitap bilgilerini girin.\n")
        import Kitap_Listesi 
        Kitap_Listesi.kitap_ekle()
        

    elif secim == "2": 
        aranan = input("Aranan kitap adı: ")
        aranan =


        if aranan in Kitap_listesi.txt:
            print (f"{aranan} kutuphanede mevcut.")
        else:
            print("Yazar:", kutuphane.get(aranan, "Bu kitap bulunamadı.\n"))
        print("Kitabin") 
    elif secim == "3": 
        for kitap, yazar in kutuphane.items(): 
        print(f"{kitap} - {yazar}") 
    elif secim == "4": 
        break 
    else: print("Geçersiz seçim.")
