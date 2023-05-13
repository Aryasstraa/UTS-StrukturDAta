import os
import queue
os.system('cls')

class myQueque:
    def __init__(self): 
        self.item = queue.Queue()

    def qAdd(self,item): #untuk menambahkan item ke dalam antrian.
        self.item.put(item)
    def isEmpty(self): # untuk memeriksa apakah antrian kosong atau tidak.
        return self.item.empty()
        
    def size(self): # untuk menghitung jumlah item dalam antrian.
        return self.item.qsize()
    
    def qOut(self):#untuk mengeluarkan 1 data
        if not self.item.empty():
            return self.item.get()
        else:
            return "Antrian Kosong" 
    
    def mainmenu(self): #untuk menampilkan menu utama dan meminta input dari pengguna.
        pilih = "y"
        while (pilih == "y"):
            os.system('cls')
            print("==========================")
            print("*     KELOMPOK 6 UTS     *")
            print("*     PROGRAM ANTRIAN PENERIMAAN BUKU DI SEKOLAH     *")
            print("==========================")
            print("1. Siswa Masuk Antrian ")
            print("2. Siswa Keluar Antrian")
            print("3. Banyaknya Antrian")
            print("4. Cek Antrian (True/False) ")
            print("5. Keluar Program")
            pilihan = str(input("Silahkan masukan pilihan anda: "))
            print("NOTE :Klik Enter Jika Ingin Melanjutkan/Out Program")
            print ("==========================")
            if (pilihan == "1"):
                nama = str(input("Masukan Nama Siswa : "))
                nis= str(input("Masukan NIS Siswa : "))
                data=[nis,nama]
                self.qAdd(data)
                print(f"NIS {nis} Atas Nama {nama} Telah Masuk Antrian")
                i = input ("")

            elif(pilihan == "2"):
                keluar = self.qOut()
                if keluar != "Antrian Kosong":
                    print("Dengan NIS",keluar[0],"Atas Nama", keluar[1],"Telah Keluar dari Antrian")
                else:
                    print("Antrian Kosong")
                i = input("")

            elif(pilihan == "3"):
                if self.size():
                    print(f"Terdapat {str(self.size())} Siswa Sedang Menunggu Antrian  ")
                else:
                    print("Tidak Ada Antrian")
                i = input("")

            elif(pilihan == "4"):
                print(self.isEmpty()) 
                i = input ("")
            
            elif(pilihan == "5"):
                print("ARIGATO KARENA SUDAH MENGGUNAKAN PROGRAM ANTRIAN PENERIMAAN BUKU DI SEKOLAH INI")
                print("SEMOGA HARIMU SENIN TERUS😜")
                print(quit())
            else:
                pilih = "n"

if __name__ == "__main__":
    q = myQueque()
    q.mainmenu()

# Penjelasan :
# Program ini memiliki beberapa fungsi, seperti siswa masuk ke dalam antrian dengan menggunakan Nama dan NIS, 
# Siswa dapat keluar dari antrian,menghitung jumlah siswa yang sedang menunggu antrian dan memeriksa apakah antrian kosong atau ada. 
# Program ini juga memiliki menu utama yang memungkinkan pengguna memilih opsi yang ingin dilakukan. 
# Program akan berjalan terus-menerus sampai pengguna memilih untuk keluar.
