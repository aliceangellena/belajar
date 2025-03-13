def hitung_biaya_perawatan(jenis_mobil,jarak_tempuh,jenis_bahan_bakar,usia_mobil,tipe_perawatan,harga_kendaraan,biaya_tambahan,waktu_parkir):
    try:  
        if jenis_mobil == "Hatchback":
            BD = 500000 + harga_kendaraan
            if  jenis_bahan_bakar == "diesel":
                BD = BD + (BD * 10/100)
                if usia_mobil > 5:
                    BD = BD + (BD * 10/100)
                    if tipe_perawatan == "rutin":
                        BD = BD + 75000
                    elif tipe_perawatan == "darurat":
                        BD = BD = 150000
                        if waktu_parkir < 0:
                            BD = BD + (BD * (25/100000 * waktu_parkir))
                            if jarak_tempuh == 0:
                                print(BD)
        
        elif jenis_mobil == "Hatchback":
            BD = 500000 + harga_kendaraan
            if  jenis_bahan_bakar == "diesel":
                BD = BD + (BD * 10/100)
                if usia_mobil > 5:
                    BD = BD + (BD * 10/100)
                    if tipe_perawatan == "rutin":
                        BD = BD + 75000
                    elif tipe_perawatan == "darurat":
                        BD = BD = 150000
                        if biaya_tambahan > 0:
                            BD = BD + biaya_tambahan
                        if waktu_parkir < 0:
                            BD = BD + (BD * (25/100000 * waktu_parkir))
                            if jarak_tempuh == 0:
                                return BD
                                 
    except:
        return("Jenis mobil tidak valid")