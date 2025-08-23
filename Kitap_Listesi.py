print("\nKITAP LISTESI\n")

kitaplar = []

def kitap_ekle():
    isim = input("Kitap adi: ")
    yazar = input("Yazar adi: ")
    yili = input("Kitabin yayin tarihi: ")

    kitaplar.append({"isim": isim, "yazar": yazar, "yil": yili})
    print("\nKitap ekleme islemi tamamlandi.")
    print(f"Kitap: {isim}, Yazar: {yazar}, Yıl: {yili}\n")
