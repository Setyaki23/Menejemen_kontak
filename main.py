kontak1 = {'nama': "Andi", 'hp': "12131425", 'email': "andi@pyhton.com"}
kontak2 = {'nama': "ANI", 'hp': "928323783", "email": "ani@aniii"}
kontak = [kontak1, kontak2]

def melihat_kontak():
    if pilihan == '1':
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        else:
            print("Kontak masih kosong")
            return 1

def menambah_kontak():
    nama = input("masukan nama yang baru: ")
    hp = input("masukan nomor hp yang baru: ")
    email = input("masukan email yang baru: ")
    kontak_baru = {"nama": nama, "hp": hp, 'email': email}
    kontak.append(kontak_baru)
    print("kontak baru berhasil ditambahkan!")
def menghapus_kontak():
    if kontak:
        for num, item in enumerate(kontak, start=1):
            print(f'\n{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
    else:
        i_hapus = int(input("masukan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus - 1]
        print("kontak sudah dihapus")


# "program manajemen kontak"#
while True:

    print("\nMenu Kontak")
    print("1.Melihat Semua Kontak")
    print("2.menambahkan kontak baru")
    print("3.menghapus Kontak")
    print("4.keluar dari kontak")

    pilihan = input("masukan pilihan  menu kontak(1,2,3 atau 4):")

    if pilihan == '1':
        melihat_kontak()
        # if kontak:
        #     for num, item in enumerate(kontak, start=1):
        #         print(f'\n{num}. {item["nama"]} ({item["hp"]}, {item["email"]})')
        # else:
        #     print("Kontak masih kosong")

    elif pilihan == '2':
        menambah_kontak()
        # menambahkan kontaK
        # nama = input("masukan nama yang baru: ")
        # hp = input("masukan nomor hp yang baru: ")
        # email = input("masukan email yang baru: ")
        # kontak_baru = {"nama": nama, "hp": hp, 'email': email}
        # kontak.append(kontak_baru)

    elif pilihan == '3':
        menghapus_kontak()

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
        break
    else:
        print("anda memasukan pilihan yang salah")
