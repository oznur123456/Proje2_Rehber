print("KITAP LISTESI OLUSTURMA\n")
print("Lutfen eklemek istediginiz kitap bilgilerini giriniz.")

def kitap_ekle():
    isim = input("Kitap adi: ")
    yazar = input("Yazar adi: ")
    yili = input("Kitabin yayin tarihi: ")
    with open("Kitap_Listesi_Olusturma.txt", "a", encoding="utf-8") as dosya: 
        dosya.write(f"Kitap: {isim}\t\t\t Yazar: {yazar}\t\t\t Yayin tarihi: {yili}\n")
    print("\nKitap ekleme islemi tamamlandi.")

    devam = input("\nBaşka işlem yapmak ister misiniz? (e/h): ").lower()
    if devam != "e":
        print("Kutuphane sistemine yönlendiriliyorsunuz...")
        import Kutuphane_Sistemi
        Kutuphane_Sistemi.kutuphane_anamenu()
    else:
        kitap_ekle()



