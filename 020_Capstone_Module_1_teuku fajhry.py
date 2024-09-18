# Capstone Module 1
# JCDS 2604020
# Teuku Muhammad Fajhry Syahputra
#------------------------------------------------------------------------------------------------------------------------


# Penjelasan terkait CAPSTONE Module 1

#     Data karyawan disimpan dalam daftar (list) yang berisi informasi karyawan seperti ID, nama, posisi, dan gaji.

#     Program ini memiliki 4 fungsi utama:
               
#               Create : Tambah Karyawan    : Menambahkan karyawan baru ke dalam daftar. 
#               Read   : Lihat Karyawan     : Menampilkan semua data karyawan.
#               Update : Perbarui Karyawan  : Mengubah data karyawan yang ada berdasarkan ID.
#               Delete : Hapus Karyawan     : Menghapus data karyawan berdasarkan ID.

#     Pengguna memilih opsi melalui menu utama, lalu memasukkan data yang diperlukan.
#     Program akan terus berjalan sampai pengguna memilih opsi untuk keluar.


#------------------------------------------------------------------------------------------------------------------------


#Data karyawan yang akan digunakan sebagai data dummy (5)

karyawan_list = [
    {'id': 1, 'nama': 'Andi', 'posisi': 'Manager', 'gaji': 12000000},
    {'id': 2, 'nama': 'Budi', 'posisi': 'Staff', 'gaji': 8000000},
    {'id': 3, 'nama': 'Cici', 'posisi': 'Supervisor', 'gaji': 10000000},
    {'id': 4, 'nama': 'Dina', 'posisi': 'HR', 'gaji': 9000000},
    {'id': 5, 'nama': 'Eko', 'posisi': 'IT Support', 'gaji': 8500000}
]


#Fungsi tampilkan data karyawan

def tampilkan_karyawan():
    for karyawan in karyawan_list:
        print(f"ID: {karyawan['id']}, Nama: {karyawan['nama']}, Posisi: {karyawan['posisi']}, Gaji: {karyawan['gaji']}")


#Fungsi tambah karyawan

def tambah_karyawan():
    id_karyawan = int(input("ID: "))
    nama = input("Nama: ")
    posisi = input("Posisi: ")
    gaji = int(input("Gaji: "))
    karyawan_list.append({'id': id_karyawan, 'nama': nama, 'posisi': posisi, 'gaji': gaji})
    print("Karyawan berhasil ditambahkan.")


#Fungsi perbarui karyawan

def perbarui_karyawan():
    id_karyawan = int(input("Masukkan ID karyawan yang akan diperbarui: "))
    for karyawan in karyawan_list:
        if karyawan['id'] == id_karyawan:
            karyawan['nama'] = input("Nama baru: ") or karyawan['nama']
            karyawan['posisi'] = input("Posisi baru: ") or karyawan['posisi']
            karyawan['gaji'] = int(input("Gaji baru: ") or karyawan['gaji'])
            print("Karyawan berhasil diperbarui.")
            return
    print("ID tidak ditemukan.")


#Fungsi hapus karyawan

def hapus_karyawan():
    id_karyawan = int(input("Masukkan ID karyawan yang akan dihapus: "))
    for karyawan in karyawan_list:
        if karyawan['id'] == id_karyawan:
            karyawan_list.remove(karyawan)
            print("Karyawan berhasil dihapus.")
            return
    print("ID tidak ditemukan.")


#Menu utama

def menu_utama():
    while True:
        print("\n1. Lihat Karyawan\n2. Tambah Karyawan\n3. Perbarui Karyawan\n4. Hapus Karyawan\n5. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            tampilkan_karyawan()
        elif pilihan == '2':
            tambah_karyawan()
        elif pilihan == '3':
            perbarui_karyawan()
        elif pilihan == '4':
            hapus_karyawan()
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


#jalankan program

if __name__ == "__main__":
    menu_utama()