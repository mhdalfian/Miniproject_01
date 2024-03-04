import os
from prettytable import PrettyTable

class Motor:
    def __init__(self, merek, tahun_pembuatan, cc_motor, kondisi, terakhir_servis):
        self.merek = merek
        self.tahun_pembuatan = tahun_pembuatan
        self.cc_motor = cc_motor
        self.kondisi = kondisi
        self.terakhir_servis = terakhir_servis
        self.next_motor = None

class Bengkel:
    def __init__(self):
        self.head = None
        motor1 = Motor("Yamaha Mio", 2019, 125, "sudah baik", 2)
        motor2 = Motor("Honda Beat", 2018, 110, "perlu perbaikan", 3)
        motor3 = Motor("Suzuki Satria", 2020, 150, "sudah baik", 1)
        motor4 = Motor("Kawasaki Ninja", 2017, 250, "ganti sparepart(modif)", 4)

        self.head = motor1
        motor1.next_motor = motor2
        motor2.next_motor = motor3
        motor3.next_motor = motor4

    def tambah_motor(self, motor, nomor_urut=None):
        if not self.head or nomor_urut == 1:
            motor.next_motor = self.head
            self.head = motor
            print("Motor", motor.merek, "telah ditambahkan di awal.")
            return

        if nomor_urut is None:
            nomor_urut = int(input("Masukkan nomor urut motor: ") or -1)

        if nomor_urut <= 0:
            if not self.head:
                self.head = motor
            else:
                current = self.head
                while current.next_motor:
                    current = current.next_motor
                current.next_motor = motor
            print("Motor", motor.merek, "telah ditambahkan di akhir.")
            return


        current = self.head
        index = 1
        while current:
            if index == nomor_urut - 1:
                motor.next_motor = current.next_motor
                current.next_motor = motor
                print("Motor", motor.merek, "telah ditambahkan sesuai nomor urut", nomor_urut - 1)
                return
            current = current.next_motor
            index += 1
        current.next_motor = motor
        print("Motor", motor.merek, "telah ditambahkan di akhir.")


    def lihat_motor(self):
        if not self.head:
            print("Belum ada motor yang terdaftar.\n")
        else:
            print("Daftar Motor:")
            table = PrettyTable(["No", "Merek", "Tahun Pembuatan", "CC Motor", "Kondisi", "Terakhir Servis(bulan)"])
            current = self.head
            index = 1
            while current:
                table.add_row([index, current.merek, current.tahun_pembuatan, current.cc_motor, current.kondisi, current.terakhir_servis])
                current = current.next_motor
                index += 1
            print(table)

    def ubah_motor(self, nomor_urut, atribut, nilai_baru):
        motor = self.cari_motor_berdasarkan_nomor_urut(nomor_urut)
        if motor:
            if atribut == 'merek':
                motor.merek = nilai_baru
                print("Berhasil mengubah merek pada motor", motor.merek)
            elif atribut == 'tahun_pembuatan':
                motor.tahun_pembuatan = nilai_baru
                print("Berhasil mengubah tahun pembuatan pada motor", motor.merek)
            elif atribut == 'cc_motor':
                motor.cc_motor = nilai_baru
                print("Berhasil mengubah CC motor pada motor", motor.merek)
            elif atribut == 'kondisi':
                motor.kondisi = nilai_baru
                print("Berhasil mengubah kondisi pada motor", motor.merek)
            elif atribut == 'terakhir_servis':
                motor.terakhir_servis = nilai_baru
                print("Berhasil mengubah terakhir servis pada motor", motor.merek)
            else:
                print("Atribut tidak valid.")
        else:
            print("Motor tidak ditemukan.")

    def hapus_motor(self, nomor_urut):
        if not self.head:
            print("Belum ada motor yang terdaftar.")
            return

        if nomor_urut == 1:
            self.head = self.head.next_motor
            print("Motor di awal telah dihapus.")
            return

        current = self.head
        index = 1
        while current.next_motor:
            if index == nomor_urut - 1:
                current.next_motor = current.next_motor.next_motor
                print("Motor nomor urut", nomor_urut, "telah dihapus.")
                return
            current = current.next_motor
            index += 1
        print("Nomor urut tidak ada. Motor tidak dihapus.")

    def cari_motor_berdasarkan_nomor_urut(self, nomor_urut):
        current = self.head
        index = 1
        while current:
            if index == nomor_urut:
                return current
            current = current.next_motor
            index += 1
        return None

def main():
    os.system("cls")
    bengkel = Bengkel()

    print("             ADMIN BENGKEL PAIN MOTOR             ")   
    while True:
        print("\nPilih Opsi yang Ingin Dilakukan:")
        print("1. Tambah Motor")
        print("2. Lihat Motor")
        print("3. Ubah Motor")
        print("4. Hapus Motor")
        print("5. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4/5): "))
        except ValueError:
            print("Masukkan angka antara 1 hingga 5.")
            continue

        os.system("cls")
        if pilihan == 1:
            print("===== TAMBAH MOTOR BARU =====\n")
            try:
                merek = input("Masukkan merek motor (nama dan merek): ")
                tahun_pembuatan = int(input("Masukkan tahun pembuatan motor: "))
                cc_motor = int(input("Masukkan CC motor: "))
                kondisi = input("Bagaimana kondisi motor? [perlu perbaikan/ganti sparepart(modif)]: ")
                terakhir_servis = int(input("Kapan terakhir kali motor di servis? (perkiraan saja dalam bulan, 1/2/3): "))
                nomor_urut = int(input("Masukkan nomor urut motor (opsional, kosongkan untuk menambahkan di akhir): ") or 0)
            except ValueError:
                print("Input harus berupa angka untuk tahun pembuatan, CC motor, dan terakhir servis.")
                continue
            
            motor_baru = Motor(merek, tahun_pembuatan, cc_motor, kondisi, terakhir_servis)
            bengkel.tambah_motor(motor_baru, nomor_urut)
        elif pilihan == 2:
            print("===== LIHAT DATA MOTOR =====\n")
            bengkel.lihat_motor()
        elif pilihan == 3:
            print("===== UBAH DATA MOTOR =====\n")
            try:
                nomor_urut = int(input("Masukkan nomor urut motor yang ingin diubah: "))
                atribut = input("Masukkan atribut yang ingin diubah (merek/tahun_pembuatan/cc_motor/kondisi/terakhir_servis): ")
                nilai_baru = input("Masukkan nilai baru: ")
            except ValueError:
                print("Masukkan nomor urut motor yang ada.")
                continue
            
            bengkel.ubah_motor(nomor_urut, atribut, nilai_baru)
        elif pilihan == 4:
            print("===== HAPUS DATA MOTOR =====\n")
            try:
                nomor_urut = int(input("Masukkan nomor urut motor yang ingin dihapus: "))
            except ValueError:
                print("Masukkan nomor urut motor yang ada.")
                continue
            
            bengkel.hapus_motor(nomor_urut)
        elif pilihan == 5:
            print("Keluar dari program. Sampai jumpa.")
            break
        else:
            print("Pilihan tidak sesuai. Kembali memilih opsi.\n")

main()

