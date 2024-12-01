import aritmatika
import bangun_datar
import bangun_ruang

# Modul Aritmatika
print("Hasil penjumlahan 7 + 3 =", aritmatika.tambah(7, 3))
print("Hasil pembagian 10 / 2 =", aritmatika.bagi(10, 2))

# Modul Bangun Datar
print("Luas persegi dengan sisi 4 =", bangun_datar.luas_persegi(4))
print("Keliling lingkaran dengan jari-jari 7 =", bangun_datar.keliling_lingkaran(7))
print("Luas trapesium dengan sisi atas 6, sisi bawah 10, dan tinggi 5 =", bangun_datar.luas_trapesium(6, 10, 5))

# Modul Bangun Ruang
print("Luas permukaan kubus dengan sisi 3 =", bangun_ruang.luas_permukaan_kubus(3))
print("Luas permukaan tabung dengan jari-jari 7 dan tinggi 10 =", bangun_ruang.luas_permukaan_tabung(7, 10))
print("Luas permukaan limas dengan alas 6, tinggi alas 4, dan tinggi limas 8 =", bangun_ruang.luas_permukaan_limas(6, 4, 8))
