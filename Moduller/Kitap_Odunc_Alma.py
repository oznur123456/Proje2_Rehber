print("KITAP ODUNC ALMA SISTEMI\n")

def odunc_al():
    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        kitaplar = dosya.readlines()

    print("Güncel Kitap Listesi:\n")
    for i, satir in enumerate(kitaplar, start=1):
        print(f"{i}. {satir.strip()}")

    try:
        secim = int(input("\nOdunc almak istediginiz kitabin numarasini giriniz: "))
        if secim < 1 or secim > len(kitaplar):
            print("Gecersiz numara.")
            return
    except ValueError:
        print("Lutfen sadece numara giriniz.")
        return

    secilen_kitap = kitaplar[secim - 1].strip()

    with open("Odunc_Alinacak_Kitaplar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(secilen_kitap + "\n")

    print(f"\n'{secilen_kitap}' odunc alma listesine eklendi.")

    devam = input("\nBaşka işlem yapmak ister misiniz? (e/h): ").lower()
    if devam != "e":
        print("Kutuphane sistemine yönlendiriliyorsunuz...")
        import Kutuphane_Sistemi
        Kutuphane_Sistemi.kutuphane_anamenu()
    else:
        odunc_al()

odunc_al()
        
