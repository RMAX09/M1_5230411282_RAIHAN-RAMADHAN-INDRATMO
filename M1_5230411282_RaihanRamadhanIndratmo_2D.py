# 2 DIMENSI (PERSEGI, PERSEGI PANJANG, LAYANG - LAYANG, BELAH KETUPAT, TRAPESIUM, JAJARANGENJANG)


def persegi(s):
    luas = s ** 2
    keliling = 4 * s
    return luas, keliling


def persegiPanjang(p, l):
    luas = p * l
    keliling = 2 * (p + l)
    return luas, keliling


def layangLayang(dg1, dg2, sPanjang, sPendek):
    luas = 0.5 * dg1 * dg2
    keliling = 2 * (sPendek + sPanjang)
    return luas, keliling


def belahKetupat(s, dg1, dg2):
    luas = 0.5 * dg1 * dg2
    keliling = 4 * s
    return luas, keliling


def trapesium(a, b, c, d, t):
    luas = 0.5 * (a + b) * t
    keliling = a + b + c + d
    return luas, keliling


def jajarangenjang(a, t, sAtas, sSamping):
    luas = a * t
    keliling = 2 * (sAtas + sSamping)
    return luas, keliling


def pilihMenu():
    print("APLIKASI HITUNG BANGUN DATAR 2D")
    print("=====PILIH BANGUN RUANG=====")
    print("1. PERSEGI")
    print("2. PERSEGI PANJANG")
    print("3. LAYANG - LAYANG")
    print("4. TRAPESIUM")
    print("5. JAJARANGENJANG")
    print("6. KELUAR")


while True:
    pilihMenu()
    inputmenu = input("Masukkan pilihan anda (1-5), 6 Keluar : ")

    if inputmenu == "1":
        s = float(input("Masukkan panjang sisi persegi: "))
        luas, keliling = persegi(s)
        print(f"Luas Persegi : {luas:.2f}")
        print(f"Keliling Persegi : {keliling:.2f}")

    elif inputmenu == "2":
        p = float(input("Masukkan panjang persegi panjang: "))
        l = float(input("Masukkan lebar persegi panjang: "))
        luas, keliling = persegiPanjang(p, l)
        print(f"Luas Persegi Panjang : {luas:.2f}")
        print(f"Keliling Persegi Panjang : {keliling:.2f}")

    elif inputmenu == "3":
        dg1 = float(input("Masukkan diagonal 1 layang - layang : "))
        dg2 = float(input("Masukkan diagonal 2 layang - layang : "))
        sPendek = float(input("Masukkan sisi pendek layang - layang : "))
        sPanjang = float(input("Masukkan sisi panjang layang - layang : "))
        luas, keliling = layangLayang(dg1, dg2, sPendek, sPanjang)
        print(f"Luas Layang - Layang : {luas:.2f}")
        print(f"Keliling Layang - Layang : {keliling:.2f}")

    elif inputmenu == "4":
        a = float(input("Masukkan sisi a : "))
        b = float(input("Masukkan sisi b : "))
        c = float(input("Masukkan sisi c : "))
        d = float(input("Masukkan sisi d : "))
        t = float(input("Masukkan tinggi trapesium : "))
        luas, keliling = trapesium(a, b, c, d, t)
        print(f"Luas Trapesium : {luas:.2f}")
        print(f"Keliling Trapesium : {keliling:.2f}")

    elif inputmenu == "5":
        a = float(input("Masukkan sisi a : "))
        t = float(input("Masukkan tinggi jajarangenjang : "))
        sAtas = float(input("Masukkan sisi atas : "))
        sBawah = float(input("Masukkan sisi bawah : "))
        luas, keliling = jajarangenjang(a, t, sAtas, sBawah)
        print(f"Luas Jajarangenjang : {luas:.2f}")
        print(f"Keliling Jajarangenjang : {keliling:.2f}")

    elif inputmenu == "6":
        print("Program berakhir, Terimakasih")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi (1-5), 6 Keluar.")
