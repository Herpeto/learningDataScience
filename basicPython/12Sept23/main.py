# main.py
from my_module import * # Menggunakan fungsi dari my_module
message = greet("Alice")
print(message) # Menggunakan variabel dari my_module

radius = 5
area = pi * square(radius)
print(f"Luas lingkaran dengan radius {radius} adalah {area:.2f}")
