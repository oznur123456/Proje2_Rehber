print("KITAP BILGILERI GUNCELLEME\n")

def kitap_degistir():
    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        satir_list = dosya.readlines()

    print("Güncel Kitap Listesi:\n")
    for i, satir in enumerate(satir_list, start=1):
        print(f"{i}. {satir.strip()}")

    degistir_numara = int(input("\nBilgilerini degistirmek istediginiz kitabin numarasini giriniz: "))

    # Kullanıcıdan yeni bilgiler
    yeni_isim = input("Yeni kitap adi: ")
    yeni_yazar = input("Yeni yazar adi: ")
    yeni_yil = input("Yeni yayin tarihi: ")

    with open("Kitap_Listesi_Olusturma.txt", "w", encoding="utf-8") as dosya:
        for i, satir in enumerate(satir_list, start=1):
            if i == degistir_numara:
                dosya.write(f"Kitap: {yeni_isim},\t\t Yazar: {yeni_yazar},\t\t Yayin tarihi: {yeni_yil}\n")
            else:
                dosya.write(satir)

    print("\nKitap kaydi basariyla guncellendi.\n")

    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        satir_list = dosya.readlines()

    print("Güncel Kitap Listesi:\n")
    for i, satir in enumerate(satir_list, start=1):
        print(f"{i}. {satir.strip()}")

kitap_degistir()
