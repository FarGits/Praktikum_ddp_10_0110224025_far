import math

def luas_permukaan_kubus(sisi):
    return 6 * (sisi ** 2)

def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

def luas_permukaan_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def luas_permukaan_limas(alas, tinggi_alas, tinggi_limas):
    luas_alas = alas * tinggi_alas
    luas_sisi = 4 * (0.5 * alas * tinggi_limas)
    return luas_alas + luas_sisi

def luas_permukaan_prisma(alas, tinggi_alas, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_alas
    luas_selimut = 2 * tinggi_prisma * (alas + tinggi_alas)
    return 2 * luas_alas + luas_selimut
