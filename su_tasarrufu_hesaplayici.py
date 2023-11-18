from tabulate import tabulate
import colorama

modlar = [
    ["1", "Yetişkin Hızlı Duş", "Ortalama yetişkinler için 10 dakikalık su verir."],
    ["2", "Yetişkin Uzun Duş", "Ortalama yetişkinler için 30 dakikalık su verir."],
    ["3", "6-12 Yaş Duş", "Ortalama 6-12 yaş arası çocuklar için 10 dakikalık su verir."],
    ["4", "Özel Hâl", "Özel durumlar için sizin ayarlamanıza olanak sağlar."]
]

def cikis():
    print(colorama.Fore.LIGHTRED_EX)
    print("Sistem kapatılıyor..")
    exit()
def islem(secimId):
    secilen_mod = [
        [modlar[secimId - 1][0], modlar[secimId - 1][1], modlar[secimId - 1][2]]
    ]
    if secimId == 1:
        genel_bilgiler = [
            ["170 Litre", "10 Dakika", "20 Litre", "1 Dakika"]
        ]
        print("\n")
        print(tabulate(genel_bilgiler, headers=["Verilecek Su Miktarı", "Verilecek Zaman", "Miktarı Aşma Hakkı", "Aşma Hakkı Süresi"]))
        onaylama = input("Çıkmak için q veya 0 tuşuna, seçiminizi onaylayarak devam etmek için 1 sayısına tıklayın: ")
        onaylama = onaylama.lower()
        if onaylama == "q" or onaylama == "0":
            cikis()
        elif onaylama == "1":
            print(colorama.Fore.LIGHTGREEN_EX)
            print("Başarılı bir şekilde sayaç çalıştırıldı.")
    elif secimId == 2:
        genel_bilgiler = [
            ["510 Litre", "30 Dakika", "40 Litre", "2 Dakika"]
        ]
        print("\n")
        print(tabulate(genel_bilgiler,
                       headers=["Verilecek Su Miktarı", "Verilecek Zaman", "Miktarı Aşma Hakkı", "Aşma Hakkı Süresi"]))
        onaylama = input("Çıkmak için q veya 0 tuşuna, seçiminizi onaylayarak devam etmek için 1 sayısına tıklayın: ")
        onaylama = onaylama.lower()
        if onaylama == "q" or onaylama == "0":
            cikis()
        elif onaylama == "1":
            print(colorama.Fore.LIGHTGREEN_EX)
            print("Başarılı bir şekilde sayaç çalıştırıldı.")
    elif secimId == 3:
        genel_bilgiler = [
            ["250 Litre", "10 Dakika", "60 Litre", "3 Dakika"]
        ]
        print("\n")
        print(tabulate(genel_bilgiler,
                       headers=["Verilecek Su Miktarı", "Verilecek Zaman", "Miktarı Aşma Hakkı", "Aşma Hakkı Süresi"]))
        onaylama = input("Çıkmak için q veya 0 tuşuna, seçiminizi onaylayarak devam etmek için 1 sayısına tıklayın: ")
        onaylama = onaylama.lower()
        if onaylama == "q" or onaylama == "0":
            cikis()
        elif onaylama == "1":
            print(colorama.Fore.LIGHTGREEN_EX)
            print("Başarılı bir şekilde sayaç çalıştırıldı.")
    elif secimId == 4:
        dus_suresi = input("Kaç dakika duşta kalacaksınız?\n--> ")
        try:
            dus_suresi = int(dus_suresi)
            yas = input("Yaşınız kaç?\n--> ")
            try:
                yas = int(yas)
                print(str(yas) + "-" + str(dus_suresi))
                if 5 < yas and yas < 10:
                    yas_litre = 23
                    toplam = dus_suresi * yas_litre
                    print(colorama.Fore.LIGHTGREEN_EX)
                    print("-" + str(dus_suresi) + "- dakika boyunca dakika başına -" + str(yas_litre) + "- litre su verilecek. Toplam -" + str(toplam) + "- litre su harcanacak.\nSistem Çalıştırıldı." )
                elif 10 < yas and yas < 15:
                    yas_litre = 27
                    toplam = dus_suresi * yas_litre
                    print(colorama.Fore.LIGHTGREEN_EX)
                    print("-" + str(dus_suresi) + "- dakika boyunca dakika başına -" + str(yas_litre) + "- litre su verilecek. Toplam -" + str(toplam) + "- litre su harcanacak.\nSistem Çalıştırıldı." )
                elif 15 < yas and yas < 22:
                    yas_litre = 28
                    toplam = dus_suresi * yas_litre
                    print(colorama.Fore.LIGHTGREEN_EX)
                    print("-" + str(dus_suresi) + "- dakika boyunca dakika başına -" + str(yas_litre) + "- litre su verilecek. Toplam -" + str(toplam) + "- litre su harcanacak.\nSistem Çalıştırıldı." )
                elif 22 < yas and yas < 35:
                    yas_litre = 29
                    toplam = dus_suresi * yas_litre
                    print(colorama.Fore.LIGHTGREEN_EX)
                    print("-" + str(dus_suresi) + "- dakika boyunca dakika başına -" + str(yas_litre) + "- litre su verilecek. Toplam -" + str(toplam) + "- litre su harcanacak.\nSistem Çalıştırıldı." )
                elif 35 < yas:
                    yas_litre = 30
                    toplam = dus_suresi * yas_litre
                    print(colorama.Fore.LIGHTGREEN_EX)
                    print("-" + str(dus_suresi) + "- dakika boyunca dakika başına -" + str(yas_litre) + "- litre su verilecek. Toplam -" + str(toplam) + "- litre su harcanacak.\nSistem Çalıştırıldı." )
            except ValueError:
                print(colorama.Fore.LIGHTRED_EX)
                print("Girilen değer bir tam sayı değil.")
                cikis()
        except ValueError:
            print(colorama.Fore.LIGHTRED_EX)
            print("Girilen değer bir tam sayı değil.")

def secim():
    secim_sayi = input("\nYapacağınız işlemin numarasını girin: ")
    secim_sayi = secim_sayi.lower()
    if secim_sayi == "1":
        islem(1)
    elif secim_sayi == "2":
        islem(2)
    elif secim_sayi == "3":
        islem(3)
    elif secim_sayi == "4":
        islem(4)
    elif secim_sayi == "q" or secim_sayi == "0":
        cikis()
def main():
    print(colorama.Fore.LIGHTWHITE_EX)
    print(tabulate(modlar, headers=["Numara", "Başlık", "Açıklama"]))
    print("Programdan çıkmak için q veya 0 tuşuna basabilirsiniz.")
    secim()


main()

#if __name__ == "__main__":
#    main()
