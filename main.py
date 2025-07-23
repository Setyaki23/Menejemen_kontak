# kontak1 = {'nama': "Andi", 'hp': "12131425", 'email': "andi@pyhton.com"}
# kontak2 = {'nama': "ANI", 'hp': "928323783", "email": "ani@aniii"}
# kontak = [kontak1, kontak2]

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)


class contac:
    def __init__(self):
        self.contac = membuka_kontak()

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
        menyimpan_kontak(isi=self.contac)

kontak_kantor = contac()
kontak_keluarga = contac()
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
        # if kontak:
        #     for num, item in enumerate(kontak, start=1):
        #         print(f'\n{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        # else:
        #     print("Kontak masih kosong")

    elif pilihan == '2':
        kontak_keluarga.menambah_kontak()
        # menambahkan kontaK
        # nama = input("masukan nama yang baru: ")
        # hp = input("masukan nomor hp yang baru: ")
        # email = input("masukan email yang baru: ")
        # kontak_baru = {"nama": nama, "hp": hp, 'email': email}
        # kontak.append(kontak_baru)

    elif pilihan == '3':
        kontak_keluarga.menghapus_kontak()

        # menghapus kontak
        # if kontak:
        #     for num, item in enumerate(kontak, start=1):
        #         print(f'\n{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        # else:
        #     print("Kontak masih kosong")
        #
        # i_hapus = int(input("masukan nomor kontak yang akan dihapus: "))
        # del kontak[i_hapus - 1]
        # print("kontak sudah dihapus")
        # continue

    elif pilihan == '4':
        # keluar dari kontak
        kontak_keluarga.keluar_kontak()
        break
    else:
        print("anda memasukan pilihan salah")
