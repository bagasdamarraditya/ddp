#1

nama_kendaraan = input("masukkan nama kendaraan?")
jenis_bensin = input("masukkan jenis bensin?")
kota_tujuan= input('Masukkan kota tujuan?')

if jenis_bensin == "pertalite":
    harga = 10000
    jarak_tempuh = 12

elif jenis_bensin == "petamax":
    harga = 14000
    jarak_tempuh = 13

elif jenis_bensin == "pertamax turbo":
    harga = 17000
    jarak_tempuh = 13.5

else :
    print ("tidak ada jenis bensin yang dipilih")

if kota_tujuan == "jakarta" :
    jarak_kota = 20

elif kota_tujuan == "bekasi" :
    jarak_kota = 35.7

elif kota_tujuan == "depok" :
    jarak_kota = 5

elif kota_tujuan == "tangerang" :
    jarak_kota = 99

elif kota_tujuan == "bogor" :
    jarak_kota = 120.6

else :
    print("tidak ada kota tujuan yang dipilih")

pemakaian_bensin = jarak_kota / jarak_tempuh
harga_total = int(pemakaian_bensin * harga)

print("nama kendaraan",nama_kendaraan)
print("jenis bensin",jenis_bensin)
print("kota yang dituju",kota_tujuan)
print("pemakaian bensin",pemakaian_bensin)
print("harga total bensin",harga_total)

#2

#3
for i in range(1,21)  :
    if i % 3 == 0 :
        print("STT Nurul Fikri")
    else :
        print (i)
