#1
def profil(nama, alamat, gender, umur, hoby):
    print("Nama",nama)
    print("Alamat",alamat)
    print("Gender",gender)
    print("Umur",umur, "Tahun")
    print("Hoby",hoby)

profil("Bagas", "Jalan Sadewa 2", "Laki-laki", "18", "Futsal")

#2
def kelulusan(nilai):
    if nilai <= 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"
    
hasil = kelulusan(15)
print (hasil)

#3
def ganjil(nilai):
    for i in range (nilai + 1):
        if i % 2 != 0 :
            print(i)
ganjil(100)

