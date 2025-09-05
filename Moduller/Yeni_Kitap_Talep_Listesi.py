print("\n YENI KITAP TALEBI \n")

def kitap_talep():
    isim = input("Kitap adi: ")
    yazar = input("Yazar adi: ")
    yili = input("Kitabin yayin tarihi: ")
    with open("Kitap_Talep_Listesi.txt", "a", encoding="utf-8") as dosya: 
        dosya.write(f"Kitap: {isim}\t\t\t Yazar: {yazar}\t\t\t Yayin tarihi: {yili}\n")
    print("\nKitap talebiniz alinmistir.")

    devam = input("\nBaşka işlem yapmak ister misiniz? (e/h): ").lower()
    if devam != "e":
        print("Kutuphane sistemine yönlendiriliyorsunuz...")
        import Kutuphane_Sistemi
        Kutuphane_Sistemi.kutuphane_anamenu()
    else:
        kitap_talep()

