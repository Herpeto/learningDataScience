def tambah(angka1,angka2):
    return angka1+angka2
def kurang(angka1,angka2):
    return angka1-angka2
def kali(angka1,angka2):
    return angka1*angka2
def bagi(angka1,angka2):
    return angka1/angka2

print("Selamat datang di kalkulator")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
print("5. Keluar")

pilihan = int(input("Masukkan nomor mode (1/2/3/4/5) : "))

while pilihan != 5:
    if(pilihan == 5):
        print("Terima kasih telah menggunakan kalkulator!")
    else:
        angka1 = int(input("Masukkan angka pertama : "))
        angka2 = int(input("Masukkan angka kedua : "))
        if(pilihan == 1):
            print(f'Hasil pertambahan {angka1} dan {angka2} = {tambah(angka1,angka2)}')
        elif(pilihan == 2):
            print(f'Hasil pengurangan {angka1} dan {angka2} = {kurang(angka1,angka2)}')
        elif(pilihan == 3):
            print(f'Hasil perkalian {angka1} dan {angka2} = {kali(angka1,angka2)}')
        elif(pilihan == 4):
            print(f'Hasil pembagian {angka1} dan {angka2} = {bagi(angka1,angka2)}')
        else:
            print("Inputan mode tidak valid!")
        
        print("Selamat datang di kalkulator")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Keluar")
        pilihan = int(input("Masukkan nomor mode (1/2/3/4/5) : "))
        
    