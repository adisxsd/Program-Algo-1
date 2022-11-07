#NURUL HADITS
#222410102043

idx = 0
print("\n")
inputKata = int(input("Masukkan Jumlah Kata : "))
print("\n")
listkata = []

for x in range(inputKata) :
    kata = input("Masukkan Kata : ")
    listkata.append (kata)

print("\nInput : ")
for x in listkata :
    print(x)

for x in listkata :
    print("\nHasil : ")
    for y in x :
        if idx < len(x) - 1 :
            if ord (x[idx]) < ord(x[idx + 1]):
                selisih = ord(x[idx+1]) - ord(x[idx])
                print((x[idx]), "lebih kecil dari", (x[idx+1]), "dan selisihnya adalah", (selisih)) 
                idx+=1
            elif ord(x[idx]) > ord(x[idx+1]) :
                selisih = ord(x[idx]) - ord(x[idx+1])
                print((x[idx]), "lebih besar dari", (x[idx+1]), "dan selisihnya adalah", (selisih))
                idx+=1
        elif idx == len (x)-1 :
            idx = 0



