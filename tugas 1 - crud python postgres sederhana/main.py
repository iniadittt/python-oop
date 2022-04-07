from connection import Connection
from mahasiswa import Mahasiswa

'''
TUGAS PBO LANJUT 1

AUTHOR  : ADITYA BAYU AJI
NIM     : 200511140
R2 - TEKNIK INFORMATIKA
'''

class Main:
    def __init__(self):
        while True:
            print('======= Aplikasi CRUD Mahasiswa =======')
            print('0. Keluar Program')
            print('1. Cari Data Mahasiswa')
            print('2. Tambah Data Mahasiswa')
            print('3. Update Data Mahasiswa')
            print('4. Hapus Data Mahasiswa')
            print('5. Tampil Semua Data Mahasiswa')
            menu = int(input('Masukkan Menu: '))
            if(menu == 0):
                break
            elif(menu == 1):
                self.search()
            elif(menu == 2):
                self.insert()
            elif(menu == 3):
                self.update()
            elif(menu == 4):
                self.delete()
            elif(menu == 5):
                self.allData()
            else:
                print('Keyowrd salah!')

    def search(self):
        try:
            print('===== CARI DATA MAHASISWA =====')
            nim = input('Masukkan NIM: ')
            print(nim)
            mhs = Mahasiswa()
            result = mhs.getByNIM(nim)
            value = mhs.affected
            if(value != 0):
                print('======= DATA MAHASISWA =======')
                print(f'NIM             : {mhs.nim}')
                print(f'Nama Mahasiswa  : {mhs.nama}')
                print(f'Jenis Kelamin   : {mhs.jk}')
            else:
                print('Data Mahasiswa Tidak Ditemukan!')
        except:
            pass

    def insert(self):
        try:
            print('===== TAMBAH DATA MAHASISWA =====')
            mhs = Mahasiswa()
            nim = input('Masukkan NIM: ')
            nama = input('Masukkan Nama Mahasiswa: ')
            jk = input('Masukkan Jenis Kelamin (L/P): ')
            jk = jk.upper()
            mhs.nim = nim
            mhs.nama = nama
            mhs.jk = jk
            simpan = mhs.simpan()
            if(simpan > 0):
                print('Data Mahasiswa Disimpan!')
            else:
                print('Data Mahasiswa Gagal Disimpan!')
        except:
            pass

    def update(self):
        try:
            print('===== UBAH DATA MAHASISWA =====')
            nim = input('Masukkan NIM: ')
            mhs = Mahasiswa()
            result = mhs.getByNIM(nim)
            value = mhs.affected
            if(value != 0):
                print('-Data Anda-')
                print(f'NIM             : {mhs.nim}')
                print(f'Nama Mahasiswa  : {mhs.nama}')
                print(f'Jenis Kelamin   : {mhs.jk}')
            else:
                print('Maaf data tidak ditemukan!')
            ubah = input('Apakah anda ingin merubah data (y/n)? ')
            ubah = ubah.lower()
            namaBaru = input('Masukkan Nama Baru: ')
            jkBaru = input('Masukkan Jenis Kelamin Baru: ')
            mhs.nim = nim
            mhs.nama = namaBaru
            mhs.jk = jkBaru
            simpan = mhs.update(nim)
            if(simpan > 0):
                print('Data Mahasiswa Diperbarui')
            else:
                print('Data Mahasiswa Gagal Diperbarui')
        except:
            pass

    def delete(self):
        try:
            print('===== HAPUS DATA MAHASISWA =====')
            nim = input('Masukkan NIM: ')
            mhs = Mahasiswa()
            simpan = mhs.delete(nim)
            if(simpan > 0):
                print('Data Mahasiswa Dihapus')
            else:
                print('Data Mahasiswa Gagal Dihapus')
        except:
            pass
    
    def allData(self):
        mhs = Mahasiswa()
        mhs.getAllData()
     
if __name__ ==  '__main__':
    app = Main()