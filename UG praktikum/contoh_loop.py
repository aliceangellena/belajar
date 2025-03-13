import random
import string
import datetime
import re

# Daftar Harga berdasarkan tipe mobil (per hari)
harga_per_tipe = {
    "SUV": 500000,
    "MPV": 400000,
    "SEDAN": 450000,
    "HATCHBACK": 350000
}

# Database Dummy (Gabungan Mobil & Transaksi)
rental_db = [
    {"ID Mobil": "M-ABC123", "Tipe": "SUV", "Harga/Hari": harga_per_tipe["SUV"], "Status": "Tersedia", "ID Transaksi": "T-XYZ123", "Nama Pelanggan": "Budi Santoso", "Tanggal Sewa": "01-02-2025", "Tanggal Kembali": "05-02-2025", "Total Harga": 2000000, "Status Pembayaran": "Lunas"},
    {"ID Mobil": "M-DEF456", "Tipe": "MPV", "Harga/Hari": harga_per_tipe["MPV"], "Status": "Tersedia", "ID Transaksi": "T-MNO456", "Nama Pelanggan": "Siti Aisyah", "Tanggal Sewa": "03-02-2025", "Tanggal Kembali": "07-02-2025", "Total Harga": 1200000, "Status Pembayaran": "Belum Lunas"},
    {"ID Mobil": "M-GHI789", "Tipe": "Sedan", "Harga/Hari": harga_per_tipe["Sedan"], "Status": "Tersedia", "ID Transaksi": "T-PQR789", "Nama Pelanggan": "Joko Widodo", "Tanggal Sewa": "05-02-2025", "Tanggal Kembali": "10-02-2025", "Total Harga": 1500000, "Status Pembayaran": "Lunas"},
    {"ID Mobil": "M-JKL012", "Tipe": "SUV", "Harga/Hari": harga_per_tipe["SUV"], "Status": "Disewa", "ID Transaksi": "T-STU012", "Nama Pelanggan": "Agus Saputra", "Tanggal Sewa": "02-02-2025", "Tanggal Kembali": "06-02-2025", "Total Harga": 1800000, "Status Pembayaran": "Belum Lunas"},
    {"ID Mobil": "M-MNO345", "Tipe": "Hatchback", "Harga/Hari": harga_per_tipe["Hatchback"], "Status": "Tersedia", "ID Transaksi": "T-VWX345", "Nama Pelanggan": "Rina Kartika", "Tanggal Sewa": "04-02-2025", "Tanggal Kembali": "08-02-2025", "Total Harga": 1000000, "Status Pembayaran": "Lunas"},
    {"ID Mobil": "M-PQR678", "Tipe": "MPV", "Harga/Hari": harga_per_tipe["MPV"], "Status": "Tersedia", "ID Transaksi": "T-YZA678", "Nama Pelanggan": "Fajar Pratama", "Tanggal Sewa": "06-02-2025", "Tanggal Kembali": "11-02-2025", "Total Harga": 1400000, "Status Pembayaran": "Belum Lunas"},
    {"ID Mobil": "M-STU901", "Tipe": "SUV", "Harga/Hari": harga_per_tipe["SUV"], "Status": "Disewa", "ID Transaksi": "T-BCD901", "Nama Pelanggan": "Dewi Lestari", "Tanggal Sewa": "07-02-2025", "Tanggal Kembali": "12-02-2025", "Total Harga": 2200000, "Status Pembayaran": "Lunas"}
]

recycle_bin = []  # Menyimpan data yang dihapus sementara

def generate_id(prefix, length=6):
    """Menghasilkan ID unik dengan kombinasi huruf dan angka."""
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# def generate_id(prefix):
#     """Membuat ID unik dengan prefix tertentu."""
#     return f"{prefix}{len(rental_db) + 1:03d}"

def input_tipe_mobil():
    """Meminta input tipe mobil dengan validasi."""
    while True:
        tipe = input("Tipe Mobil (SUV, MPV, Sedan, Hatchback): ").strip().upper()
        if tipe in harga_per_tipe:
            return tipe, harga_per_tipe[tipe]
        print("Tipe mobil tidak valid! Pilih dari: SUV, MPV, Sedan, Hatchback.")

def input_status_mobil():
    """Meminta input status mobil dengan validasi."""
    while True:
        status = input("Status Mobil (Tersedia/Terpakai): ").strip().capitalize()
        if status in ["Tersedia", "Terpakai"]:
            return status
        print("Status mobil tidak valid! Masukkan 'Tersedia' atau 'Terpakai'.")

def input_nama_pelanggan():
    """Meminta input nama pelanggan dengan validasi."""
    while True:
        nama = input("Nama Pelanggan: ").strip()
        if nama.replace(" ", "").isalpha():
            return nama
        print("Nama pelanggan hanya boleh berisi huruf! Silakan coba lagi.")

def input_tanggal_sewa_kembali():
    """Meminta input tanggal sewa dan kembali dengan validasi."""
    while True:
        try:
            tanggal_sewa_str = input("Tanggal Sewa (DD-MM-YYYY): ").strip()
            tanggal_kembali_str = input("Tanggal Kembali (DD-MM-YYYY): ").strip()

            tanggal_sewa = datetime.datetime.strptime(tanggal_sewa_str, "%d-%m-%Y")
            tanggal_kembali = datetime.datetime.strptime(tanggal_kembali_str, "%d-%m-%Y")

            jumlah_hari = (tanggal_kembali - tanggal_sewa).days
            if jumlah_hari <= 0:
                raise ValueError("Tanggal kembali harus lebih besar dari tanggal sewa.")

            return tanggal_sewa_str, tanggal_kembali_str, jumlah_hari
        except ValueError as e:
            print(f"Error: {e}. Silakan coba lagi.")

def input_status_pembayaran():
    """Meminta input status pembayaran dengan validasi."""
    while True:
        status = input("Status Pembayaran (Lunas/Belum Lunas): ").strip().title()
        if status in ["Lunas", "Belum Lunas"]:
            return status
        print("Status pembayaran tidak valid! Masukkan 'Lunas' atau 'Belum Lunas'.")

def create_rental():
    """Menambah mobil baru dan transaksi sewa ke dalam sistem."""
    print("\n=== Tambah Mobil & Transaksi ===")

    id_mobil = generate_id("M-")
    id_transaksi = generate_id("T-")
    tipe, harga_per_hari = input_tipe_mobil()
    status_mobil = input_status_mobil()
    nama_pelanggan = input_nama_pelanggan()
    tanggal_sewa_str, tanggal_kembali_str, jumlah_hari = input_tanggal_sewa_kembali()
    total_harga = harga_per_hari * jumlah_hari
    status_pembayaran = input_status_pembayaran()

    # Simpan data rental
    rental_db.append({
        "ID Mobil": id_mobil,
        "Tipe": tipe,
        "Harga/Hari": harga_per_hari,
        "Status": status_mobil,
        "ID Transaksi": id_transaksi,
        "Nama Pelanggan": nama_pelanggan,
        "Tanggal Sewa": tanggal_sewa_str,
        "Tanggal Kembali": tanggal_kembali_str,
        "Total Harga": total_harga,
        "Status Pembayaran": status_pembayaran
    })

    print("\nMobil dan transaksi berhasil ditambahkan!")

def read_rental():
    """Menampilkan semua data rental atau memfilter berdasarkan Tipe Mobil, Status, dan Status Pembayaran."""
    while True:
        try:
            print("\n=== Data Rental ===")
            print("\nFilter Data Rental:")
            print("1. Semua Data")
            print("2. Berdasarkan Tipe Mobil")
            print("3. Berdasarkan Status Mobil")
            print("4. Berdasarkan Status Pembayaran")
            print("5. Kembali ke Menu Utama")

            pilihan = input("Pilih opsi filter (1-5): ").strip()

            if pilihan == "1":
                data_filtered = rental_db
            elif pilihan == "2":
                tipe = input("Masukkan tipe mobil: ").strip().capitalize()
                data_filtered = [rental for rental in rental_db if rental["Tipe"] == tipe]
            elif pilihan == "3":
                status = input("Masukkan status mobil: ").strip().capitalize()
                data_filtered = [rental for rental in rental_db if rental["Status"] == status]
            elif pilihan == "4":
                status_pembayaran = input("Masukkan status pembayaran: ").strip().capitalize()
                data_filtered = [rental for rental in rental_db if rental["Status Pembayaran"] == status_pembayaran]
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid! Silakan coba lagi.")
                continue

            print(tabulate(data_filtered, headers="keys", tablefmt="grid"))
        except Exception as e:
            print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")

def update_rental():
    """Mengedit data rental dengan pilihan kolom. Jika tanggal atau harga berubah, total harga diperbarui otomatis."""
    if not rental_db:
        print("Database rental kosong.")
        return

    print("\n=== Update Data Rental ===")


    id_edit = input("\nMasukkan ID Mobil atau ID Transaksi yang ingin diedit: ").strip()
    rental_data = None

    # Mencari data berdasarkan ID Mobil atau ID Transaksi
    for rental in rental_db:
        if rental["ID Mobil"] == id_edit or rental["ID Transaksi"] == id_edit:
            rental_data = rental
            break

    if not rental_data:
        print(f"Data dengan ID '{id_edit}' tidak ditemukan.")
        return

    print("\nData ditemukan. Silakan pilih kolom yang ingin diubah.")

    while True:
        print("\nKolom yang dapat diedit:")
        print("1. Nama Pelanggan")
        print("2. Tipe Mobil")
        print("3. Tanggal Sewa")
        print("4. Tanggal Kembali")
        print("5. Harga/Hari")
        print("6. Selesai & Kembali ke Menu Utama")

        pilihan = input("Pilih nomor kolom yang ingin diedit: ").strip()

        if pilihan == "1":  # Edit Nama Pelanggan
            new_nama = input(f"Nama Pelanggan [{rental_data['Nama Pelanggan']}]: ").strip()
            if new_nama:
                if re.match(r"^[A-Za-z\s]+$", new_nama):  # Hanya huruf dan spasi
                    rental_data["Nama Pelanggan"] = new_nama
                else:
                    print("Nama hanya boleh mengandung huruf dan spasi!")

        elif pilihan == "2":  # Edit Tipe Mobil
            print("Pilihan tipe mobil: SUV, MPV, Sedan")
            new_tipe = input(f"Tipe Mobil [{rental_data['Tipe']}]: ").strip().upper()
            if new_tipe in harga_per_tipe:
                rental_data["Tipe"] = new_tipe
                rental_data["Harga/Hari"] = harga_per_tipe[new_tipe]  # Update harga berdasarkan tipe
                print(f"Harga/Hari otomatis diperbarui menjadi {rental_data['Harga/Hari']}.")

        elif pilihan == "3":  # Edit Tanggal Sewa
            new_tgl_sewa = input(f"Tanggal Sewa [{rental_data['Tanggal Sewa']}]: ").strip()
            if new_tgl_sewa:
                if re.match(r"^\d{2}-\d{2}-\d{4}$", new_tgl_sewa):  # Format dd-mm-yyyy
                    rental_data["Tanggal Sewa"] = new_tgl_sewa
                else:
                    print("Format tanggal harus dd-mm-yyyy!")

        elif pilihan == "4":  # Edit Tanggal Kembali
            new_tgl_kembali = input(f"Tanggal Kembali [{rental_data['Tanggal Kembali']}]: ").strip()
            if new_tgl_kembali:
                if re.match(r"^\d{2}-\d{2}-\d{4}$", new_tgl_kembali):  # Format dd-mm-yyyy
                    rental_data["Tanggal Kembali"] = new_tgl_kembali
                else:
                    print("Format tanggal harus dd-mm-yyyy!")

        elif pilihan == "5":  # Edit Harga per Hari
            new_harga_hari = input(f"Harga/Hari [{rental_data['Harga/Hari']}]: ").strip()
            if new_harga_hari.isdigit():
                rental_data["Harga/Hari"] = int(new_harga_hari)
            else:
                print("Harga per hari harus berupa angka!")

        elif pilihan == "6":
            print("Kembali ke menu utama.")
            break

        else:
            print("Pilihan tidak valid! Silakan pilih kembali.")

        # Menghitung Durasi (Tanggal Kembali - Tanggal Sewa)
        try:
            tgl_sewa = datetime.datetime.strptime(rental_data["Tanggal Sewa"], "%d-%m-%Y")
            tgl_kembali = datetime.datetime.strptime(rental_data["Tanggal Kembali"], "%d-%m-%Y")
            rental_data["Durasi (hari)"] = (tgl_kembali - tgl_sewa).days

            if rental_data["Durasi (hari)"] < 0:
                print("Tanggal kembali tidak boleh lebih awal dari tanggal sewa!")
                continue
        except ValueError:
            print("Tanggal tidak valid, pastikan format dd-mm-yyyy!")
            continue

        # Perbarui Total Harga setelah perubahan
        rental_data["Total Harga"] = rental_data["Durasi (hari)"] * rental_data["Harga/Hari"]

        print("\nData berhasil diperbarui!")
        print(tabulate([rental_data], headers="keys", tablefmt="grid"))

        while True:
            lanjut = input("\nEdit kolom lain? (y/n): ").strip().lower()
            if lanjut == "y":
                break  # Kembali ke pemilihan kolom untuk diedit
            elif lanjut == "n":
                print("Kembali ke menu utama.")
                return  # Keluar dari seluruh loop dan program
            else:
                print("Hanya boleh memasukkan 'y' atau 'n'. Silakan coba lagi.")

def delete_rental():
    """Menghapus data rental dan menyimpannya di recycle bin."""
    while True:
        try:
            print("\n=== Hapus Data Rental ===")
            id_mobil = input("Masukkan ID Mobil atau ID Transaksi yang ingin dihapus: ")
            found = False
            for rental in rental_db:
                if rental["ID Mobil"] == id_mobil or rental["ID Transaksi"] == id_mobil:
                    rental_db.remove(rental)
                    recycle_bin.append(rental)
                    print(f"Data rental untuk mobil {id_mobil} telah dihapus dan dipindahkan ke recycle bin.")
                    found = True
                    break
            if not found:
                print(f"ID Mobil atau ID Transaksi {id_mobil} tidak ditemukan.")
            break  # keluar dari loop setelah menghapus data
        except ValueError as ve:
            print(f"Error: {ve}. Silakan coba lagi.")

def read_recycle_bin():
    """Menampilkan data yang telah dihapus dan memberikan opsi untuk mengembalikan data."""
    while True:
        try:
            print("\n=== Recycle Bin ===")
            if len(recycle_bin) == 0:
                print("Tidak ada data di recycle bin.")
                break  # keluar dari loop jika recycle bin kosong

            # Menampilkan data di recycle bin
            print(tabulate(recycle_bin, headers="keys", tablefmt="grid"))

            # Opsi untuk mengembalikan data
            pilihan = input("Ingin mengembalikan data? (Y/N): ").strip().lower()
            if pilihan == "y":
                id_restore = input("Masukkan ID Mobil atau ID Transaksi yang ingin dikembalikan: ").strip()

                # Mencari data di recycle bin
                for rental in recycle_bin:
                    if rental["ID Mobil"] == id_restore or rental["ID Transaksi"] == id_restore:
                        rental_db.append(rental)  # Mengembalikan ke database utama
                        recycle_bin.remove(rental)  # Menghapus dari recycle bin
                        print(f"Data dengan ID {id_restore} telah dikembalikan ke rental database.")
                        break
                else:
                    print(f"ID {id_restore} tidak ditemukan di recycle bin.")

            elif pilihan == "n":
                break  # keluar jika tidak ingin mengembalikan data
            else:
                print("Pilihan tidak valid! Masukkan 'Y' untuk ya atau 'N' untuk tidak.")

        except ValueError as ve:
            print(f"Error: {ve}. Silakan coba lagi.")

def crud_data():
    while True:
        try:
            print("\n=== Sistem Rental Mobil ===")
            print("1. Tambah Mobil & Transaksi")
            print("2. Lihat Data Rental")
            print("3. Update Status Mobil atau Pembayaran")
            print("4. Hapus Data Rental")
            print("5. Lihat Recycle Bin")
            print("6. Keluar")
            choice = input("Pilih menu: ")
            if choice == "1": create_rental()
            elif choice == "2": read_rental()
            elif choice == "3": update_rental()
            elif choice == "4": delete_rental()
            elif choice == "5": read_recycle_bin()
            elif choice == "6": break
            else:
                print("Pilihan tidak valid!")
        except ValueError as ve:
            print(f"Error: {ve}. Silakan coba lagi.")

# Fungsi Perhitungan Tagihan dan Diskon
def hitung_pembayaran(total_harga):
    if total_harga >= 1500000:
        diskon = total_harga * 0.2
    elif total_harga > 1000000:
        diskon = total_harga * 0.1
    else:
        diskon = 0

    total_setelah_diskon = total_harga - diskon
    print(f"\nTagihan: Rp {total_harga:,}")
    print(f"Diskon: Rp {diskon:,}")
    print(f"Total setelah diskon: Rp {total_setelah_diskon:,}")

    while True:
        try:
            jumlah_bayar = int(input("Masukkan jumlah uang yang dibayarkan: Rp "))
            if jumlah_bayar < total_setelah_diskon:
                kurang = total_setelah_diskon - jumlah_bayar
                print(f"Pembayaran anda kurang: Rp {kurang:,} \nStatus: Belum Lunas")
                return "Belum Lunas", jumlah_bayar - total_setelah_diskon
            elif jumlah_bayar == total_setelah_diskon:
                print("Pembayaran anda pas!! \nStatus: Lunas")
                return "Lunas", 0
            else:
                kembalian = jumlah_bayar - total_setelah_diskon
                print(f"Pembayaran anda lebih! Kembalian: Rp {kembalian:,} \nStatus: Lunas")
                return "Lunas", kembalian
        except ValueError:
            print("Input tidak valid! Masukkan angka.")

# Fungsi Pembelian Mobil (REUSABLE dari Fitur Create Rental)
def pembelian():
    print("\n=== Pembelian Mobil ===")

    tipe, harga_per_hari = input_tipe_mobil()
    nama_pelanggan = input_nama_pelanggan()
    tanggal_sewa, tanggal_kembali, jumlah_hari = input_tanggal_sewa_kembali()

    total_harga = harga_per_hari * jumlah_hari
    status_pembayaran, kembalian = hitung_pembayaran(total_harga)

    # Simpan data transaksi pembelian
    rental_db.append({
        "ID Mobil": generate_id("M-"),
        "Tipe": tipe,
        "Harga/Hari": harga_per_hari,
        "Status": "Tersedia",
        "ID Transaksi": generate_id("T-"),
        "Nama Pelanggan": nama_pelanggan,
        "Tanggal Sewa": tanggal_sewa,
        "Tanggal Kembali": tanggal_kembali,
        "Total Harga": total_harga,
        "Status Pembayaran": status_pembayaran
    })

    print("\n✅ Transaksi berhasil disimpan!")

# Fungsi Main (Menu Utama)
def main():
    while True:
        print("\n=== Sistem Rental Mobil ===")
        print("1. Sebagai Admin")
        print("2. Sebagai Pembeli")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ").strip()
        if pilihan == "1":
            crud_data()
        elif pilihan == "2":
            pembelian()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem rental mobil.")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

main()