daftar_belanja = []

def data_input_daftar(data):
    daftar_belanja.append(data)
    print(f'{data} telah dimasukkan kedalam daftar belanja.')

def data_hapus_daftar(data):
    if(data in daftar_belanja):
        print(f'{data} telah dihapuskan dari daftar belanja')
    else:
        print(f'{data} tidak ditemukan di daftar belanja!')

def data_print_daftar():
    print("List daftar belanja : ")
    for i in range(len(daftar_belanja)):
        print(f'{i+1}. {daftar_belanja[i]}')