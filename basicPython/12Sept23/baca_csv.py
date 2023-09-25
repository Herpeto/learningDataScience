import csv

def baca_data_csv(nama_file):
    data = []
    with open (nama_file, mode = 'r') as file:
        data_csv = csv.DictReader(file)

        for readData in data_csv:
            data.append(readData)
    return data

def tulis_data_csv(nama_file, data):
    with open(nama_file, mode='w', newline='') as file:
        judul = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=judul)
        writer.writeheader()
        writer.writerows(data)

nama_file = 'test.csv'
data_produk = baca_data_csv(nama_file)
print("Data Produk : ")
for data in data_produk:
    print(f"{data['nama']} : Rp.{data['harga']}, Stok : {data['stok']}")
