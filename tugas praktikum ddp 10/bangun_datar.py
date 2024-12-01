import math

# Persegi
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

# Persegi Panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

# Segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(a, b, c):
    return a + b + c

# Lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

def keliling_lingkaran(jari_jari):
    return 2 * math.pi * jari_jari

# Trapesium
def luas_trapesium(sisi_atas, sisi_bawah, tinggi):
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi

def keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_d):
    return sisi_a + sisi_b + sisi_c + sisi_d
