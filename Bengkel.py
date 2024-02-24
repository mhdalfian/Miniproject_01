import os
from prettytable import PrettyTable

class Motor:
    def __init__(self, merek, tahun_pembuatan, cc_motor, kondisi, terakhir_servis):
        self.info_motor = {
            'merek': merek,
            'tahun_pembuatan': tahun_pembuatan,
            'cc_motor': cc_motor,
            'kondisi': kondisi,
            'terakhir_servis': terakhir_servis
        }

    def update_atribut(self, atribut, nilai_baru):
        if atribut in self.info_motor:
            self.info_motor[atribut] = nilai_baru
            print("Berhasil mengubah", atribut, "pada motor", self.info_motor['merek'])
        else:
            print("Atribut tidak valid.")

class Bengkel:
    def __init__(self):
        self.daftar_motor = {}

    def tambah_motor(self, motor):
        self.daftar_motor[motor.info_motor['merek']] = motor
        print("Motor", motor.info_motor['merek'], "telah ditambahkan.")


    def lihat_motor(self):
        if self.daftar_motor:
            print("Daftar Motor:")
            table = PrettyTable(["Merek", "Tahun Pembuatan", "CC Motor", "Kondisi", "Terakhir Servis(bulan)"])
            for motor in self.daftar_motor.values():
                info = motor.info_motor
                table.add_row([info['merek'], info['tahun_pembuatan'], info['cc_motor'], info['kondisi'], info['terakhir_servis']])
            print(table)
        else:
            print("Belum ada motor yang terdaftar.\n")

    def ubah_motor(self, merek, atribut, nilai_baru):
        if merek in self.daftar_motor:
            motor = self.daftar_motor[merek]
            if atribut in motor.info_motor:
                motor.update_atribut(atribut, nilai_baru)
            else:
                print("Atribut yang dimasukkan tidak sesuai.")
        else:
            print("Motor tidak ditemukan.")

    def hapus_motor(self, merek):
        if merek in self.daftar_motor:
            del self.daftar_motor[merek]
            print("Motor", merek, "telah dihapus.")
        else:
            print("Motor tidak ditemukan.")

    def tampil_info_motor(self, motor):
        info = motor.info_motor
        print("Merek:", info['merek'])
        print("Tahun pembuatan:", info['tahun_pembuatan'])
        print("CC motor:", info['cc_motor'])
        print("Kondisi motor:", info['kondisi'])
        print("Terakhir di servis:", info['terakhir_servis'])


def main():
    os.system("cls")
    bengkel = Bengkel()

    print("             SELAMAT DATANG DI BENGKEL PAIN MOTOR             ")   
    print("   Menyediakan jasa servis motor, ganti sparepart motor, dll   ")
    while True:
        print("\nPilih Opsi yang Ingin Dilakukan:")
        print("1. Tambah Motor")
        print("2. Lihat Motor")
        print("3. Ubah Motor")
        print("4. Hapus Motor")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
        os.system("cls")
        if pilihan == '1':
            print("===== TAMBAH MOTOR BARU =====\n")
            while True:
                merek = input("Masukkan merek motor (nama dan merek): ")
                try:
                    tahun_pembuatan = int(input("Masukkan tahun pembuatan motor: "))
                    cc_motor = int(input("Masukkan CC motor: "))
                    kondisi = input("Bagaimana kondisi motor? [perlu perbaikan/ganti sparepart(modif)]: ")
                    terakhir_servis = int(input("Kapan terakhir kali motor di servis? (perkiraan saja dalam bulan, 1/2/3): "))
                    break
                except ValueError:
                    print("\nTipe data yang dimasukkan tidak sesuai, perhatikan apakah angka atau huruf.") 
                    print("Mohon masukkan kembali.")

            motor_baru = Motor(merek, tahun_pembuatan, cc_motor, kondisi, terakhir_servis)
            bengkel.tambah_motor(motor_baru)
        elif pilihan == '2':
            print("===== LIHAT DATA MOTOR =====\n")
            bengkel.lihat_motor()
        elif pilihan == '3':
            print("===== UBAH DATA MOTOR =====\n")
            merek_motor = input("Masukkan merek motor yang ingin diubah (sesuai yang anda input): ")
            atribut = input("Masukkan atribut yang ingin diubah (semua huruf harus kecil, ubah spasi memakai underline'_'): ")
            nilai_baru = input("Masukkan nilai baru: ")
            bengkel.ubah_motor(merek_motor, atribut, nilai_baru)
        elif pilihan == '4':
            print("===== HAPUS DATA MOTOR =====\n")
            merek_motor = input("Masukkan merek motor yang ingin dihapus: ")
            bengkel.hapus_motor(merek_motor)
        elif pilihan == '5':
            print("Terima kasih telah berkunjung. Sampai jumpa.")
            break
        else:
            print("Pilihan tidak sesuai. Kembali memilih opsi.\n")

main()
