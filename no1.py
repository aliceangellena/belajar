def perkalian(angka, pengali):
    hasil = 0
    proses = []
    
    for i in range(pengali):
        hasil += angka
        proses.append(str(angka))
    
    # Format output
    proses_str = "+".join(proses)
    print(f"{angka}x{pengali}={proses_str}={hasil}")

# Contoh penggunaan
perkalian(6, 5)  # Output: 6x5=5+5+5+5+5+5=30
perkalian(7, 10) # Output: 7x10=10+10+10+10+10+10+10=70