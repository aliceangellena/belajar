def ganjil(bawah, atas):
    # Cek apakah batas bawah lebih kecil dari batas atas
    if bawah < atas:
        # Iterasi dari kecil ke besar
        for i in range(bawah, atas + 1):
            if i % 2 != 0:  # Cek apakah bilangan ganjil
                print(i, end=", " if i < atas - 1 else "\n")
    else:
        # Iterasi dari besar ke kecil
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:  # Cek apakah bilangan ganjil
                print(i, end=", " if i > atas + 1 else "\n")

# Contoh penggunaan
print("bawah = 10, atas = 30")
ganjil(10, 30)  # Output: 11, 13, 15, 17, 19, 21, 23, 25, 27, 29

print("\nbawah = 97, atas = 82")
ganjil(97, 82)  # Output: 97, 95, 93, 91, 89, 87, 85, 83