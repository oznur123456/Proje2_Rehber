print("KITAP BILGILERI DEGISTIRME\n")

def kitap_degistir():
    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        satir_list = [satir.strip() for satir in dosya.readlines()]

    kitap_listesi = []
    for satir in satir_list:
        parcalar = satir.split(", ")
        if len(parcalar) == 3:
            try:
                isim = parcalar[0].split(": ", 1)[1]
                yazar = parcalar[1].split(": ", 1)[1]
                yil = parcalar[2].split(": ", 1)[1]
                kitap_listesi.append([isim, yazar, yil])
            except IndexError:
                continue

    if not kitap_listesi:
        print("Güncel kitap listesi boş veya format hatalı.\n")
        return

    for i, kitap in enumerate(kitap_listesi, start=1):
        print(f"{i}. Kitap: {kitap[0]}, Yazar: {kitap[1]}, Yayin tarihi: {kitap[2]}")

    degistir_numara = int(input("\nBilgilerini degistirmek istediginiz kitabin numarasini giriniz: "))
    if degistir_numara < 1 or degistir_numara > len(kitap_listesi):
        print("Geçersiz numara.\n")
        return

    secilen_kitap = kitap_listesi[degistir_numara - 1]
    isim, yazar, yil = secilen_kitap

    print("\nHangi bilgiyi degistirmek istiyorsunuz?")
    print("1. Kitap adi")
    print("2. Yazar")
    print("3. Yayin tarihi")
    secim = input("Seciminizi yapin (1/2/3): ")

    if secim == "1":
        isim = input("Yeni kitap adi: ")
    elif secim == "2":
        yazar = input("Yeni yazar adi: ")
    elif secim == "3":
        yil = input("Yeni yayin tarihi: ")

    kitap_listesi[degistir_numara - 1] = [isim, yazar, yil]

    with open("Kitap_Listesi_Olusturma.txt", "w", encoding="utf-8") as dosya:
        for kitap in kitap_listesi:
            dosya.write(f"Kitap: {kitap[0]}, Yazar: {kitap[1]}, Yayin tarihi: {kitap[2]}\n")

    print("\nKitap kaydi basariyla guncellendi.\n")

    for i, kitap in enumerate(kitap_listesi, start=1):
        print(f"{i}. Kitap: {kitap[0]}, Yazar: {kitap[1]}, Yayin tarihi: {kitap[2]}")

kitap_degistir()
