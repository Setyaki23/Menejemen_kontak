#untuk menjalakan fungsi kontak




import DOKUMEN


class contac:
    def __init__(self):
        self.contac =DOKUMEN.membuka_kontak()

    def melihat_kontak(self):
        if self.contac:
            for num, item in enumerate(self.contac, start=1):
                print(f'{num}. ' + item)
        else:
            print("Kontak masih kosong")
            return 1



    def menambah_kontak(self):
        nama = input("masukan nama yang baru: ")
        hp = input("masukan nomor hp yang baru: ")
        email = input("masukan email yang baru: ")
        kontak_baru = f'{nama} ({hp}, {email})' + '\n'
        self.contac.append(kontak_baru)
        print("kontak baru berhasil ditambahkan!")

    def menghapus_kontak(self):
        if self.melihat_kontak()== 1:
            return

        else:
            try:
                i_hapus = int(input("masukan nomor kontak yang akan dihapus: "))
                del self.contac[i_hapus - 1]
                print("kontak sudah dihapus")
            except:
                print('input yang anda masukan salah')

    def keluar_kontak(self):
       DOKUMEN.menyimpan_kontak(isi=self.contac)
