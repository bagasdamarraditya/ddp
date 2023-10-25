#true
a = 'saya'
jajan = 30000

if (jajan <= 30000):
    keterangan = 'jajan cukup'
else:
    keterangan = 'jajan berlebih'
print (a,'jajan hari ini sebesar', jajan, keterangan)

#false
b = 'saya'
jamtidur = '10 malam'

if (jamtidur > '10 malam'):
    keterangan = 'tidur cukup'
else:
    keterangan = 'tidur tidak cukup'
print (b,'tidur jam', jamtidur, keterangan)

#elif
c = 'bagas'
isibensin = 46000

if (isibensin == 50000):
    keterangan = 'bensin full tank'
elif (isibensin >= 45000):
    keterangan = 'bensin hampir full tank'
else:
    keterangan = 'bensin terisi sedikit'
print ('pelanggan',c, 'bensin anda Rp.', isibensin, keterangan)

# nliai
nama = 'Bagas Damar Raditya'
kelas = 'SI03'
nim = '0110123286'
matkul = 'ddp'
nilai = 85

if (nilai >= 90):
    keterangan = 'grade A'
elif (nilai >= 80):
    keterangan = 'grade B'
elif (nilai >= 70 ):
    keterangan = 'grade C'
else:
    keterangan = 'grade D'
print(nama,kelas,nim, 'Grade Anda pada matkul', matkul, 'adalah',keterangan )