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


kitaplari_goster()