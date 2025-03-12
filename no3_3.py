def hitung_ips():
    # Input jumlah mata kuliah
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

    total_bobot = 0
    total_sks = 0

    # Loop untuk setiap mata kuliah
    for i in range(1, jumlah_matkul + 1):
        print(f"\nMata kuliah ke-{i}")
        nilai = input("Masukkan nilai (A, B, C, atau D): ").upper()

        # Tentukan bobot nilai
        if nilai == "A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            print("Nilai tidak valid. Harap masukkan A, B, C, atau D.")
            return  # Keluar dari fungsi jika nilai tidak valid

        # Diasumsikan SKS setiap mata kuliah adalah 3
        sks = 3
        total_bobot += bobot * sks
        total_sks += sks

    # Hitung IPS
    if total_sks == 0:
        print("Tidak ada mata kuliah yang dihitung.")
    else:
        ips = total_bobot / total_sks
        print(f"\nIndeks Prestasi Semester (IPS) Anda adalah: {ips:.2f}")

# Jalankan program
hitung_ips()