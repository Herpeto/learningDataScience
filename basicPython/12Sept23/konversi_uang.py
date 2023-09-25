from currency_converter import CurrencyConverter
c = CurrencyConverter()

jumlah_USD = float(input("Masukkan jumlah USD yang ingin di convert ke IDR : "))
print("Hasil Convert : Rp. %.2f"%(c.convert(jumlah_USD,'USD','IDR')))