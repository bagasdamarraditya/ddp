#fungsi nilai
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def predikatlulus(data) :
    lulus = [mahasiswa['nama'] 
             for mahasiswa in data 
             if mahasiswa['nilai'] > 65]
    return lulus
        
hasil = predikatlulus(hasil_akhir)
print('mahasiswa yang lulus :', hasil)

#fungsi buah terbalik
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah) :
    list_terbalik = []
    for i in range(len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik

hasil = list_buah(buah)
print(hasil)

#fungsi duplikasi
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(buah):
    list_baru = []
    for i in buah:
        list_baru.append(i)
        list_baru.append(i)
    return list_baru

hasil = duplikasi(buah)
print(hasil)

#string konsonan
def konsonan(kalimat):
    huruf = ""

    for i in kalimat:
        if i not in 'aiueo':
            huruf += i
    return huruf

hasilnya = konsonan('Nurul Fikri')
print('huruf konsonan dari kata nurul fikri adalah',hasilnya)

