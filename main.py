
import kontak
def main():
    kontak_kantor =kontak.contac()
    kontak_keluarga =kontak.contac()
    # "program manajemen kontak"#
    while True:

        print("\nMenu Kontak")
        print("1.Melihat Semua Kontak")
        print("2.menambahkan kontak baru")
        print("3.menghapus Kontak")
        print("4.keluar dari kontak")

        pilihan = input("masukan pilihan  menu kontak(1,2,3 atau 4):")

        if pilihan == '1':
            kontak_keluarga.melihat_kontak()

        elif pilihan == '2':
            kontak_keluarga.menambah_kontak()

        elif pilihan == '3':
            kontak_keluarga.menghapus_kontak()



        elif pilihan == '4':
            # keluar dari kontak
            kontak_keluarga.keluar_kontak()
            break
        else:
            print("anda memasukan pilihan salah")
if __name__ =="__main__":
    main()