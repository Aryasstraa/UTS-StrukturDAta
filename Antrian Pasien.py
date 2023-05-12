import os
import queue
os.system('cls')

class myQueque:
    def __init__(self): 
        self.item = queue.Queue()

    def qAdd(self, item): #untuk menambahkan item ke dalam antrian.
        self.item.put(item)

    def isEmpty(self): # untuk memeriksa apakah antrian kosong atau tidak.
        return self.item.empty()

    def qOut(self): #untuk mengeluarkan item dari antrian.
        if not self.item.empty():
            return self.item.get()
        else:
            return " Antrian Pasien Kosong"
        
    def size(self): # untuk menghitung jumlah item dalam antrian.
        return self.item.qsize()
    
    def mainmenu(self): #untuk menampilkan menu utama dan meminta input dari pengguna.
        pilih = "y"
        while (pilih == "y"):
            os.system('cls')
            print("==========================")
            print("*     KELOMPOK 6 UTS     *")
            print("==========================")
            print("1. Masuk Antrian Pasien")
            print("2. Keluar Antrian Pasien")
            print("3. Cek Antrian")
            print("4. Banyak Antrian Pasien")
            print("5. Keluar Program")
            pilihan = str(input("Silahkan masukan pilihan anda: "))
            print("NOTE :Klik Enter Jika Ingin Melanjutkan/Out Program")
            print ("==========================")
            if (pilihan == "1"):
                obj = str(input("Masukan Nama Pasien : "))
                self.qAdd(obj)
                print(f"Pasien {obj} Telah masuk Antrian")
                i = input ("")

            elif(pilihan == "2"):
                keluar = self.qOut()
                if keluar != "Nama Pasien Kosong":
                    print(f"Pasien {keluar} Keluar Dari Antrian ")
                else:
                    print ("Antiran Pasien Kosong")
                i = input ("")

            elif(pilihan == "3"):
                print(self.isEmpty()) 
                i = input ("")

            elif(pilihan == "4"):
                print(f"Terdapat {str(self.size())} Pasien Sedang Menunggu Antrian  ")
                i = input("")
            
            elif(pilihan == "5"):
                print("ARIGATO KARENA SUDAH MENGGUNAKAN PROGRAM ANTRIAN PASIEN INI")
                print("SEMOGA HARIMU SENIN TERUS😜")
                print(quit())
            else:
                pilih = "n"

if __name__ == "__main__":
    q = myQueque()
    q.mainmenu()

# Penjelasan :
# Program ini memiliki beberapa fungsi, seperti menambahkan pasien ke dalam antrian, 
# menghapus pasien dari antrian, memeriksa apakah antrian kosong,dan menghitung jumlah pasien dalam antrian. 
# Program ini juga memiliki menu utama yang memungkinkan pengguna memilih opsi yang ingin dilakukan. 
# Program akan berjalan terus-menerus sampai pengguna memilih untuk keluar.
