teks = """Ini adalah contoh teks.
Teks ini digunakan untuk latihan pencarian kata."""

kata_cari = input("Masukkan kata yang ingin dicari : ")

if(kata_cari in teks):
    print(f'Kata "{kata_cari}" ada di teks')
else:
    print(f'Kata "{kata_cari}" tidak ada di teks')
    