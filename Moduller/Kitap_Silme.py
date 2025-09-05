print("KITAP KAYDI SILME\n")

with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
    satir_list = dosya.readlines()

print("Güncel Kitap Listesi:\n")
for i, satir in enumerate(satir_list, start=1):
    print(f"{i}. {satir.strip()}")

sil_numara = int(input("\nSilmek istediginiz kitabin numarasini giriniz: "))

with open("Kitap_Listesi_Olusturma.txt", "w", encoding="utf-8") as dosya:
    for i, satir in enumerate(satir_list, start=1):
        if i != sil_numara:
            dosya.write(satir)

print("\nKitap kaydi basariyla silindi.\n")

with open("Kitap_Listesi_Olusturma.txt", "r", encoding="utf-8") as dosya:
    satir_list = dosya.readlines()

print("Güncel Kitap Listesi:\n")
for i, satir in enumerate(satir_list, start=1):
    print(f"{i}. {satir.strip()}")