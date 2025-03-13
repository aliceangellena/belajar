a = int(input("Masukkan angka: "))
b = int(input("Masukkan angka Pengali: "))

def perkalian(a, b):
    hasil = 0
    for i in range(a):
        hasil += b
    return hasil

print(f"{a} x {b} = {perkalian(a, b)}.")