print("\nGUNCEL KITAP LISTESI\n")

def kitaplari_goster():
    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()

    if not satirlar:
        print("Su anda kutuphanede kayitli kitap yok.\n")
    else:
        print("Güncel Kitap Listesi:\n")
        for i, satir in enumerate(satirlar, start=1):
            print(f"{i}. {satir.strip()}")
        print("\n")

    devam = int(input("\nKutuphane sistemine donmek icin 1'e basiniz. ").lower())
    if devam == 1:
        print("Kutuphane sistemine yonlendiriliyorsunuz...")
        import Kutuphane_Sistemi
        Kutuphane_Sistemi.kutuphane_anamenu()
    else:
        print ("Lutfen 1'e basiniz.")
        kitaplari_goster()

kitaplari_goster()



