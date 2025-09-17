import databasebank as db
def menu_nasabah():
    while True:
        print("\n--- Manajemen Nasabah ---")
        print("1. Tambah Nasabah Baru")
        print("2. Tampilkan Semua Nasabah")
        print("3. Perbarui Email Nasabah")
        print("4. Hapus Nasabah")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            print("\n-- Menambahkan Nasabah Baru --")
            nama = input("Nama Lengkap: ")
            alamat = input("Alamat: ")
            email = input("Email: ")
            telepon = input("Nomor Telepon: ")
            db.tambah_nasabah(nama, alamat, email, telepon)
        elif pilihan == '2':
            db.lihat_semua_nasabah()
        elif pilihan == '3':
            nasabah_id = input("Masukkan ID Nasabah yang akan diupdate: ")
            email_baru = input("Masukkan Email baru: ")
            db.update_email_nasabah(nasabah_id, email_baru)
        elif pilihan == '4':
            nasabah_id = input("Masukkan ID Nasabah yang akan dihapus: ")
            db.hapus_nasabah(nasabah_id)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

def menu_rekening():
    while True:
        print("\n--- Manajemen Rekening ---")
        print("1. Buka Rekening Baru")
        print("2. Lihat Rekening Berdasarkan Nasabah")
        print("3. Setor Tunai (Tambah Saldo)")
        print("4. Lihat Saldo Spesifik")
        print("5. Tutup Rekening")
        print("6. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            print("\n-- Membuka Rekening Baru --")
            try:
                nasabah_id = int(input("Masukkan ID Nasabah pemilik: "))
                nomor_rekening = input("Masukkan Nomor Rekening baru: ")
                jenis_rekening = input("Jenis Rekening (Tabungan/Giro): ")
                db.buka_rekening(nasabah_id, nomor_rekening, jenis_rekening)
            except ValueError:
                print("❌ Input tidak valid. ID Nasabah harus berupa angka.")
        elif pilihan == '2':
            try:
                nasabah_id = int(input("Masukkan ID Nasabah: "))
                db.lihat_rekening_nasabah(nasabah_id)
            except ValueError:
                print("❌ Input tidak valid. ID Nasabah harus berupa angka.")
        elif pilihan == '3':
            print("\n-- Setor Tunai --")
            try:
                rekening_id = int(input("Masukkan ID Rekening tujuan: "))
                jumlah = float(input("Masukkan jumlah setoran: "))
                if jumlah <= 0:
                    print("❌ Jumlah setoran harus lebih dari nol.")
                else:
                    db.buat_transaksi(rekening_id, 'KREDIT', jumlah, "Setor Tunai")
            except ValueError:
                print("❌ Input tidak valid. ID dan jumlah harus berupa angka.")
        elif pilihan == '4':
            print("\n-- Cek Saldo Rekening --")
            try:
                rekening_id = int(input("Masukkan ID Rekening yang akan dicek: "))
                db.lihat_saldo(rekening_id)
            except ValueError:
                print("❌ Input tidak valid. ID Rekening harus berupa angka.")
        elif pilihan == '5':
            print("\n-- Menutup Rekening --")
            try:
                rekening_id = int(input("Masukkan ID Rekening yang akan ditutup: "))
                db.tutup_rekening(rekening_id)
            except ValueError:
                print("❌ Input tidak valid. ID Rekening harus berupa angka.")
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid.")
            
def menu_transaksi():
    while True:
        print("\n--- Manajemen Transaksi ---")
        print("1. Buat Transaksi Baru")
        print("2. Lihat Riwayat Transaksi Rekening")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih opsi (1-3): ")

        if pilihan == '1':
            print("\n-- Membuat Transaksi Baru --")
            rekening_id = int(input("Masukkan ID Rekening: "))
            tipe_transaksi = input("Tipe (DEBIT/KREDIT): ")
            jumlah = float(input("Jumlah: "))
            deskripsi = input("Deskripsi: ")
            db.buat_transaksi(rekening_id, tipe_transaksi, jumlah, deskripsi)
        elif pilihan == '2':
            rekening_id = int(input("Masukkan ID Rekening: "))
            db.lihat_riwayat_transaksi(rekening_id)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")

# --- FUNGSI UTAMA ---

def main():
    """Fungsi utama untuk menjalankan loop aplikasi."""
    while True:
        print("\n======= MENU UTAMA APLIKASI BANK =======")
        print("1. Manajemen Nasabah")
        print("2. Manajemen Rekening")
        print("3. Manajemen Transaksi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            menu_nasabah()
        elif pilihan == '2':
            menu_rekening()
        elif pilihan == '3':
            menu_transaksi()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
