from Kitap_Listesi_Olusturma import kitaplar

kitaplar_kume = set((k["isim"], k["yazar"], k["yil"]) for k in kitaplar)

def kitaplari_goster():
    if not kitaplar_kume:
        print("Su anda kutuphanede kayitli kitap yok.\n")
    else:
        print("Güncel Kitap Listesi:\n")
        for i, kitap in enumerate(kitaplar_kume, start=1):
            print(f"{i}. {kitap[0]} | Yazar: {kitap[1]} | Yıl: {kitap[2]}")
        print("\n")

kitaplari_goster()