print("\n KUTUPHANE KITAP ARAMA MENUSU \n")

def aranan_kitap():
    aranan = input("Aranan kitap adi: ").strip().lower()

    bulundu = False
    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya:
            if satir.startswith("Kitap:"):
                # "Kitap:" kısmını temizle ve "Yazar:" kısmına kadar al
                kitap_adi = satir.replace("Kitap:", "").split("Yazar:")[0].strip().lower()

                if aranan == kitap_adi:
                    print(f"'{kitap_adi.title()}' adi kitap kutuphanede mevcut.")
                    bulundu = True
                    break

    if not bulundu:
        print("Aradiginiz kitap kutuphanede mevcut degil.")

    devam = input("\nBaska islem yapmak ister misiniz? (e/h): ").lower()
    if devam == "e":
        aranan_kitap()
    else:
        print("Kutuphane sistemine yonlendiriliyorsunuz...")
        import Kutuphane_Sistemi
        Kutuphane_Sistemi.kutuphane_anamenu()

