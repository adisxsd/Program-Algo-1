#NURUL HADITS
#222410102043

sapi_warrior = 690
sapi_mage = 420
sapi_assasin = 530
sapi_nolep = 330
a = 0
print("\n")
print('Jenis-jenis sapi : ')
print('1. Sapi Warrior : 690 hari')
print('2. Sapi Mage : 420 hari')
print('3. Sapi Assasin : 530 hari')
print('4. Sapi Nolep : 330 hari')
print("\n")
b = []
c = []
inputSapi = int(input("Masukkan Jumlah Sapi : "))
for x in range (inputSapi):
    kodeSapi= int(input("Input Kode sapi :  "))
    b.append(kodeSapi)
    if kodeSapi == 1 :
        c.append(sapi_warrior)
    elif kodeSapi == 2 :
        c.append(sapi_mage)
    elif kodeSapi == 3 :
        c.append(sapi_assasin)
    elif kodeSapi == 4 :
        c.append(sapi_nolep)
    elif kodeSapi != 1 or kodeSapi !=2 or kodeSapi != 3 or kodeSapi != 4 :
        print("Kode Sapi Tidak Tersedia")
        exit()

for x in b :
    print(x)
jumlah = sum(c)
totalTahun = int(jumlah/365)
totalBulan = int((jumlah/365)/30)
totalHari = int(jumlah - (totalTahun*365) - (totalBulan*30))
print(f"Lama waktu yang dibutuhkan adalah {totalTahun} Tahun, {totalBulan} Bulan, {totalHari}, Hari")


