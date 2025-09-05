def kitap_odunc():

    with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
        satir_list = dosya.readlines()
        for satir in dosya: 
            print("-->", satir.strip())
