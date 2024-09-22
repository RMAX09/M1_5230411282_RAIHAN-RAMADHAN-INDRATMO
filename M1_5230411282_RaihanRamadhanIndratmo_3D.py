import math

# 3 DIMENSI


def tabung(jari_jari, tinggi):
    volume = math.pi * (jari_jari ** 2) * tinggi
    luasPermukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return volume, luasPermukaan


def kubus(sisi):
    volume = sisi ** 3
    luasPermukaan = 6 * (sisi ** 2)
    return volume, luasPermukaan


def bola(jari_jari):
    volume = 4/3 * math.pi * (jari_jari ** 3)
    luasPermukaan = 4 * math.pi * (jari_jari ** 2)
    return volume, luasPermukaan


def menu():
    print("APLIKASI HITUNG BANGUN RUANG 3D")
    print("=====PILIH BANGUN RUANG=====")
    print("1. TABUNG")
    print("2. KUBUS")
    print("3. BOLA")
    print("4. KELUAR")


while True:
    menu()
    inputmenu = input("Masukkan pilihan anda (1-3), 4 Keluar : ")

    if inputmenu == "1":
        jari_jari = float(input("Masukkan jari - jari tabung : "))
        tinggi = float(input("Masukkan tinggi tabung : "))
        volume, luasPermukaan = tabung(jari_jari, tinggi)
        print(f"Volume Tabung : {volume:.2f}")
        print(f"Luas Permukaan Tabung : {luasPermukaan:.2f}")

    elif inputmenu == "2":
        sisi = float(input("Masukkan sisi kubus : "))
        volume, luasPermukaan = kubus(sisi)
        print(f"Volume Kubus : {volume:.2f}")
        print(f"Luas Permukaan Kubus : {luasPermukaan:.2f}")

    elif inputmenu == "3":
        jari_jari = float(input("Masukkan jari - jari bola : "))
        volume, luasPermukaan = bola(jari_jari)
        print(f"Volume Bola : {volume:.2f}")
        print(f"Luas Permukaan Bola : {luasPermukaan:.2f}")

    elif inputmenu == "4":
        print("Program berakhir, Terimakasih")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi (1-3), 4 Keluar.")
