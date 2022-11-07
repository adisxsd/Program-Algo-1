a=True
list1 = []
kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

print("\n")
kata=input("Masukkan Kata: ")
print("\nInput : ")
print(kata)

print("\nOutput :")
for x in range(len(kata)-1 ) :
    if kata[x] in kiri :
        if kata[x+1] in kiri :
            print("False")
            print(f"Penjelasan : Karakter yang berdempetan yakni, '{kata[x]}' , dan, '{kata[x+1]}', berada di satu tangan kiri")
            a=False
    if kata[x] in kanan :
        if kata[x+1] in kanan :
            print("False")
            print(f"Penjelasan : Karakter yang berdempetan yakni '{kata[x]}', dan , '{kata[x+1]}' , berada di satu tangan kanan ")
            a=False
if a == True :
    print("\n")
    print("Output : ")
    print("True")
    print("Penjelasan : Setiap karakater selalu bergantian tangan.")


