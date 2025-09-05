print("\n KITAP ARAMA MENUSU \n")

def aranan_kitap():
    aranan = input("Aranan kitap adi: ").strip()

    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya:
            if satir.startswith("Kitap: "):
                kitap_adi = satir.split(",")[0].replace("Kitap: ", "").strip()
                if aranan.lower() == kitap_adi.lower():
                    print(f"{aranan} adli kitap kutuphanede mevcut.")
                    return
    print("Aradiginiz kitap kutuphanede mevcut degil.")

aranan_kitap()