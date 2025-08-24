print("\n KITAP ARAMA MENUSU \n")

import Guncel_Kitap_Listesi 
Guncel_Kitap_Listesi.kitaplari_goster()

def aranan_kitap():
    aranan = input("Aranan kitap adi: ")

    with open("Kitap_listesi.txt", "r", encoding="utf-8") as f:
        kitaplar = f.read().splitlines()

    if aranan in kitaplar:
        print(f"{aranan} kütüphanede mevcut.")
    else:
        print("Aradiginiz kitap kutuphanede mevcut degil.)