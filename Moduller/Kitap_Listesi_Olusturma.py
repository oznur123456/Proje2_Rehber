print("KITAP LISTESI\n")
print ("Lutfen eklemek istediginiz kitap bilgilerini giriniz.")
isim = input("Kitap adi: ")
yazar = input("Yazar adi: ")
yili = input("Kitabin yayin tarihi: ")

def kitap_ekle():
    with open ("Kitap_Listesi_Olusturma.txt", "a", encoding="utf-8") as dosya: 
        dosya.write(f"Kitap: {isim}, Yazar: {yazar}, Yayin tarihi: {yili}\n")
    print("\nKitap ekleme islemi tamamlandi.")

kitap_ekle()
