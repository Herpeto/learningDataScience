def hitung_bmi(berat, tinggi):
    tinggi = tinggi/100
    return (berat/(tinggi**2))

def kategori_bmi(bmi):
    if(bmi < 18.5):
        return 'Underweight'
    elif(bmi > 18.5 and bmi < 24.9):
        return 'Normal'
    elif(bmi > 25 and bmi < 29.9):
        return 'Overweight'
    else:
        return 'Obesitas'
    
berat = float(input("Masukkan berat anda : "))
tinggi = float(input("Masukkan tinggi anda (dalam CM) : "))

bmi = hitung_bmi(berat,tinggi)
print(f'Dengan berat {berat} dan tinggi {tinggi}')
print(f'BMI anda adalah : {bmi} dan termasuk kategori {kategori_bmi(bmi)}')
