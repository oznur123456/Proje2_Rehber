print("KITAP LISTESI\n")
print("Lutfen eklemek istediginiz kitap bilgilerini giriniz.")

def kitap_ekle():
    isim = input("Kitap adi: ")
    yazar = input("Yazar adi: ")
    yili = input("Kitabin yayin tarihi: ")
    with open("Kitap_Listesi_Olusturma.txt", "a", encoding="utf-8") as dosya: 
        dosya.write(f"Kitap: {isim}\t\t\t Yazar: {yazar}\t\t\t Yayin tarihi: {yili}\n")
    print("\nKitap ekleme islemi tamamlandi.")

kitap_ekle()

