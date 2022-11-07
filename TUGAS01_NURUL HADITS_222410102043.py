# NAMA : NURUL HADITS
# NIM  : 222410102043



print(2*'=', "Program  Angka Gasal dan Genap", 2* '=')

a1 = int(input("\nMasukkan Angka : "))
if (a1 %2 == 0 and a1 <10) : 
    print("Bilangan tersebut adalah bilangan genap dan termasuk dalam nilai kecil")
elif(a1 %2 == 0 and a1 >=10 and a1 <50) :
    print("Bilangan tersebut adalah bilangan genap dan termasuk dalam nilai sedang")
elif(a1 %2 == 0 and a1 >=50 and a1 <100 ) :
    print("Bilangan tersebut adalah bilangan genap dan termasuk dalam nilai besar")
elif(a1 %2 != 0 and a1 < 10) :
    print("Bilangan tersebut adalah bilangan gasal dan termasuk dalam nilai kecil")
elif(a1 %2 != 0 and a1 >= 10 and a1 < 50) :
    print("Bilangan tersebut adalah bilangan gasal dan termasuk dalam nilai sedang")
elif(a1 %2 != 0 and a1 >=50 ) :
    print("Bilangan tersebut adalah bilangan gasal dan termasuk dalam nilai besar")

print(2* '=', "Terima Kasih !", 2* '=') 