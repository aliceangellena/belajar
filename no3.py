def hitung_ips():
    # Input jumlah mata kuliah
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))
    
    total_nilai = 0
    total_sks = 0
    
    # Bobot nilai
    bobot_nilai = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 1
    }
    
    # Loop untuk setiap mata kuliah
    for i in range(jumlah_mata_kuliah):
        nilai = input(f"Masukkan nilai untuk mata kuliah {i + 1} (A/B/C/D): ").upper()
        
        # Cek apakah nilai valid
        if nilai in bobot_nilai:
            # Setiap mata kuliah memiliki 3 SKS
            sks = 3
            total_nilai += bobot_nilai[nilai] * sks
            total_sks += sks
        else:
            print("Nilai tidak valid. Silakan masukkan A, B, C, atau D.")
            return  # Keluar dari fungsi jika nilai tidak valid

    # Hitung IPS
    if total_sks > 0:
        ips = total_nilai / total_sks
        print(f"IPS yang didapat: {ips:.2f}")
    else:
        print("Tidak ada SKS yang dihitung.")

# Jalankan program
hitung_ips()