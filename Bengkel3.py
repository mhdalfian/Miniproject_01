import os  # Import modul os untuk membersihkan layar konsol
from prettytable import PrettyTable  # Import class PrettyTable dari modul prettytable

class Motor:
    def __init__(self, merek, tahun_pembuatan, cc_motor, kondisi, terakhir_servis):
        # Inisialisasi atribut-atribut objek Motor
        self.merek = merek
        self.tahun_pembuatan = tahun_pembuatan
        self.cc_motor = cc_motor
        self.kondisi = kondisi
        self.terakhir_servis = terakhir_servis
        self.next_motor = None  # Pointer ke motor berikutnya dalam linked list

class Bengkel:
    def __init__(self):
        self.head = None  # Inisialisasi kepala linked list Motor
        # Pembuatan beberapa objek Motor awal
        motor1 = Motor("Yamaha Mio", 2019, 125, "sudah baik", 2)
        motor2 = Motor("Honda Beat", 2018, 110, "perlu perbaikan", 3)
        motor3 = Motor("Suzuki Satria", 2020, 150, "sudah baik", 1)
        motor4 = Motor("Kawasaki Ninja", 2017, 250, "ganti sparepart(modif)", 4)
        # Penyusunan linked list dengan motor1 sebagai kepala
        self.head = motor1
        motor1.next_motor = motor2
        motor2.next_motor = motor3
        motor3.next_motor = motor4

    def tambah_motor(self, motor, nomor_urut=None):
        # Metode untuk menambahkan motor ke linked list
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
        # Metode untuk menampilkan daftar motor
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
        # Metode untuk mengubah atribut motor tertentu
        motor = self.cari_motor_berdasarkan_nomor_urut(nomor_urut)
        if motor:
            if atribut == 'merek':
                motor.merek = nilai_baru
                print("Berhasil mengubah merek pada motor", motor.merek)
            elif atribut == 'tahun_pembuatan':
                try:
                    # Validasi apakah nilai_baru adalah angka
                    nilai_baru = int(nilai_baru)
                except ValueError:
                    print("Masukkan angka untuk tahun pembuatan.")
                    return
                # Simpan tahun pembuatan motor sebelum diubah
                tahun_sebelumnya = motor.tahun_pembuatan
                motor.tahun_pembuatan = nilai_baru
                print("Berhasil mengubah tahun pembuatan pada motor", motor.merek)
                # Jika tahun pembuatan berubah, perbarui linked list dengan melakukan sorting berdasarkan tahun pembuatan
                if tahun_sebelumnya != nilai_baru:
                    self.head = self.merge_sort_tahun(self.head, ascending=True)
            elif atribut == 'cc_motor':
                try:
                    motor.cc_motor = int(nilai_baru)
                except ValueError:
                    print("Masukkan angka untuk CC motor.")
                    return
                print("Berhasil mengubah CC motor pada motor", motor.merek)
            elif atribut == 'kondisi':
                motor.kondisi = nilai_baru
                print("Berhasil mengubah kondisi pada motor", motor.merek)
            elif atribut == 'terakhir_servis':
                try:
                    motor.terakhir_servis = int(nilai_baru)
                except ValueError:
                    print("Masukkan angka untuk terakhir servis.")
                    return
                print("Berhasil mengubah terakhir servis pada motor", motor.merek)
            else:
                print("Atribut tidak valid.")
        else:
            print("Motor tidak ditemukan.")



    def hapus_motor(self, nomor_urut):
        # Metode untuk menghapus motor dari linked list
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
        # Metode untuk mencari motor berdasarkan nomor urut
        current = self.head
        index = 1
        while current:
            if index == nomor_urut:
                return current
            current = current.next_motor
            index += 1
        return None

    def merge_sort_tahun(self, head, ascending=True):
        # Metode untuk melakukan sorting linked list berdasarkan tahun pembuatan motor
        if not head or not head.next_motor:
            return head

        # Fungsi untuk membagi linked list menjadi dua bagian
        def split_list(head):
            pointer1 = head
            pointer2 = head.next_motor

            while pointer2 and pointer2.next_motor:
                pointer1 = pointer1.next_motor
                pointer2 = pointer2.next_motor.next_motor

            tengah = pointer1.next_motor
            pointer1.next_motor = None
            return head, tengah

        # Fungsi untuk menggabungkan dua linked list yang sudah diurutkan
        def merge(kiri, kanan):
            if not kiri:
                return kanan
            if not kanan:
                return kiri

            if ascending:
                if kiri.tahun_pembuatan <= kanan.tahun_pembuatan:
                    hasil = kiri
                    hasil.next_motor = merge(kiri.next_motor, kanan)
                else:
                    hasil = kanan
                    hasil.next_motor = merge(kiri, kanan.next_motor)
            else:
                if kiri.tahun_pembuatan >= kanan.tahun_pembuatan:
                    hasil = kiri
                    hasil.next_motor = merge(kiri.next_motor, kanan)
                else:
                    hasil = kanan
                    hasil.next_motor = merge(kiri, kanan.next_motor)

            return hasil

        kiri, kanan = split_list(head)

        kiri = self.merge_sort_tahun(kiri, ascending)
        kanan = self.merge_sort_tahun(kanan, ascending)

        return merge(kiri, kanan)

    def merge_sort_merek(self, head, ascending=True):
        # Metode untuk melakukan sorting linked list berdasarkan merek motor
        if not head or not head.next_motor:
            return head

        # Fungsi untuk membagi linked list menjadi dua bagian
        def split_list(head):
            pointer1 = head
            pointer2 = head.next_motor

            while pointer2 and pointer2.next_motor:
                pointer1 = pointer1.next_motor
                pointer2 = pointer2.next_motor.next_motor

            tengah = pointer1.next_motor
            pointer1.next_motor = None
            return head, tengah

        # Fungsi untuk menggabungkan dua linked list yang sudah diurutkan
        def merge(kiri, kanan):
            if not kiri:
                return kanan
            if not kanan:
                return kiri

            if ascending:
                if kiri.merek.lower() <= kanan.merek.lower():
                    hasil = kiri
                    hasil.next_motor = merge(kiri.next_motor, kanan)
                else:
                    hasil = kanan
                    hasil.next_motor = merge(kiri, kanan.next_motor)
            else:
                if kiri.merek.lower() >= kanan.merek.lower():
                    hasil = kiri
                    hasil.next_motor = merge(kiri.next_motor, kanan)
                else:
                    hasil = kanan
                    hasil.next_motor = merge(kiri, kanan.next_motor)

            return hasil

        kiri, kanan = split_list(head)
        kiri = self.merge_sort_merek(kiri, ascending)
        kanan = self.merge_sort_merek(kanan, ascending)

        return merge(kiri, kanan)

def main():
    os.system("cls")  # Membersihkan layar konsol
    bengkel = Bengkel()  # Membuat objek variable Bengkel

    print("             ADMIN BENGKEL PAIN MOTOR             ")   
    while True:
        print("\nPilih Opsi yang Ingin Dilakukan:")
        print("1. Tambah Motor")
        print("2. Lihat Motor")
        print("3. Ubah Motor")
        print("4. Hapus Motor")
        print("5. Sorting secara ascending")
        print("6. Sorting secara descending")
        print("7. Keluar")

        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4/5/6/7): "))  # Menerima input pilihan dari pengguna
        except ValueError:
            print("Masukkan angka antara 1 hingga 7.")
            continue

        os.system("cls")  # Membersihkan layar konsol
        if pilihan == 1:
            print("===== TAMBAH MOTOR BARU =====\n")
            try:
                # Menerima input informasi motor baru
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
            # Lakukan sorting berdasarkan merek setelah menambah motor baru
            bengkel.head = bengkel.merge_sort_merek(bengkel.head, ascending=True)
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
            print("===== Sorting Ascending =====\n")
            print("Pilih kriteria sorting:")
            print("1. Berdasarkan tahun pembuatan motor")
            print("2. Berdasarkan abjad huruf merek motor")

            try:
                kriteria = int(input("Masukkan pilihan (1/2): "))
            except ValueError:
                print("Masukkan angka antara 1 atau 2.")
                continue

            if kriteria == 1:
                print("===== Sorting secara ascending berdasarkan tahun pembuatan =====\n")
                bengkel.head = bengkel.merge_sort_tahun(bengkel.head, ascending=True)
                bengkel.lihat_motor()
            elif kriteria == 2:
                print("===== Sorting secara ascending berdasarkan merek =====\n")
                bengkel.head = bengkel.merge_sort_merek(bengkel.head, ascending=True)
                bengkel.lihat_motor()
            else:
                print("Pilihan tidak valid.")
        elif pilihan == 6:
            print("===== Sorting Descending =====\n")
            print("Pilih kriteria sorting:")
            print("1. Berdasarkan tahun pembuatan motor")
            print("2. Berdasarkan abjad huruf merek motor")

            try:
                kriteria = int(input("Masukkan pilihan (1/2): "))
            except ValueError:
                print("Masukkan angka antara 1 atau 2.")
                continue

            if kriteria == 1:
                print("===== Sorting secara descending berdasarkan tahun pembuatan =====\n")
                bengkel.head = bengkel.merge_sort_tahun(bengkel.head, ascending=False)
                bengkel.lihat_motor()
            elif kriteria == 2:
                print("===== Sorting secara descending berdasarkan merek =====\n")
                bengkel.head = bengkel.merge_sort_merek(bengkel.head, ascending=False)
                bengkel.lihat_motor()
            else:
                print("Pilihan tidak valid.")
        elif pilihan == 7:
            print("Keluar dari program. Sampai jumpa.")
            break
        else:
            print("Pilihan tidak sesuai. Kembali memilih opsi.\n")


main()
