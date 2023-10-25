#Membuat list kendaraan
kendaraan = ['Vario','Motor','156cc','Hitam','2 Roda']
print(kendaraan)

#menambahkan harga kendaraan dan tipe kendaraan
kendaraan.append('Rp.30.000.000')
kendaraan.append('Vario 160')
print(kendaraan)

#menambahkan merk kendaraan di index 2
kendaraan.insert(2,'Honda')
print(kendaraan)

#
ket = '''Selamat datang di aplikasi menghitung luas bangun datar masukan pilihan :
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga
'''

pilih = input(ket)

match pilih:
    case '1':
        print('kamu milih 1 untuk menghitung luas persegi')
        sisi = int(input('masukan sisinya'))
        luasP = sisi*sisi
        print('Luas persegi yang sisinya',sisi,'adalah',luasP)
    case '2':
        print('kamu memilih 2 untuk menghitung luas lingkaran')
        jari2 = float(input('masukan jari jari ?'))
        luasL = 3.14 * jari2 * jari2
        print('luas lingkaran yang jari-jarinya', jari2,'adalah',int(luasL))
    case '3':
        print('kamu memilih 3 untuk menghitung luas segitiga')
        alas = int(input('maskan alas ?'))
        tinggi = int(input ('masukan tinggi?'))
        luasS = 0.5 * alas * tinggi
        print ('luas segitiga yang alasnya',alas,'dan tingginya',tinggi,'adalah',int(luasS))
    case _:
        print('salah memilih pilihan')