class Cetacea :
    def tittle(self):
        print("\t\t\t\t\t\t=======================")
        print("\t\t\t\t\t\t\t Cetacea ")
        print("\t\t\t\t\t\t=======================\n")
        
    def intro(self):
        print("\tOrdo Cetacea adalah mamalia yang memiliki adaptasi terbaik untuk hidup di lingkungan laut. Hewan dari ordo ini bernafas menggunakan paru-paru, dengan sesekali mereka terlihat naik ke permukaan air untuk melakukan pertukaran udara.")

    def jenis(self):
        print("\n\tSecara umum, Cetacea dibagi menjadi dua sub ordo, yaitu Odontoceti dan Mysticeti. Odontoceti adalah kumpulan dari Cetacea yang memiliki gigi, sedangkan Mysticeti adalah kumpulan Cetacea yang memiliki baleen (rambut di dalam mulut yang berfungsi untuk menyaring makanan.")
        print("\nContoh spesies cetacea :")

    def footer(self):
        print("\n\t\t\t\t\t\t=======================")
        print("\t\t\t\t\t\t\t Thanks ")
        print("\t\t\t\t\t\t=======================\n")

class PausBungkuk(Cetacea):
    def jenis(self):
        print("\n* Paus Bungkuk termasuk ke dalam sub-ordo Mysticeti")

class LumbaMoncongPanjang(Cetacea):
    def jenis(self):
        print("\n* Lumba-lumba Moncong Panjang termasuk ke dalam sub-ordo Odontoceti")

class PesutMahakam(Cetacea):
    def jenis(self):
        print("\n* Pesut Mahakam termasuk sub-ordo Odontoceti")

obj_cetacea = Cetacea()
obj_pausbungkuk = PausBungkuk()
obj_lumbamoncongpanjang = LumbaMoncongPanjang()
obj_pesutmahakam = PesutMahakam()

obj_cetacea.tittle()
obj_cetacea.intro()
obj_cetacea.jenis()

obj_pausbungkuk.jenis()

obj_lumbamoncongpanjang.jenis()

obj_pesutmahakam.jenis()

obj_cetacea.footer()