class tokoabc:
    datajl = [{"nmbrg": "Tissue", "harga": 4000},
              {"nmbrg": "Minyak", "harga": 3000},
              {"nmbrg": "Telur", "harga": 25000},
              {"nmbrg": "Keju", "harga": 15000},
              {"nmbrg": "Tepung", "harga": 25000},
              {"nmbrg": "Beras", "harga": 13500},
              {"nmbrg": "Mie", "harga": 3000},
              {"nmbrg": "Gula", "harga": 8500}
             ]
    
    def __init__(self):
        self.brg = []
        self.harga = 0
        
    def getHargaTotal(self, jumlah):  
        return float(self.harga) * jumlah
    
    def daftarhrg(self):
        print("==========================")
        print("Selamat datang di Toko Abc")
        print("Silahkan Pilih Belanja Anda: ")
        print("1. Teh          Rp 4000/item")
        print("2. Minyak       Rp 30000/L")
        print("3. Telur        Rp 25000/kg")
        print("4. Keju         Rp 15000/item")
        print("5. Tepung       Rp 25000/kg")
        print("6. Beras        Rp 13500/kg")
        print("7. Mie          Rp 3000/item")
        print("8. Gula         Rp 8500/item")
        
        def pilihblj(self):
            brg = int(input("Masukkan barang belanja: "))
            if brg > 8:
                print("belanja ada tidak tersedia. ")
                self.pilihblj()
            else:
                nama = self.datajl[brg - 1]
                print("Belanja anda" + nama["nmbrg"] + "dengan harga Rp" +str(nama["harga"]))
                banyak = int(input("Jumlah belanja : "))
                tlblj = banyak * nama["harga"]
                self.harga += tlblj
                print(tlblj)
                self.item.append(nama["nmbrg"] + "x" + str(banyak) + "Rp" + str(tlblj))
                print("Pilih Belanja Tambahan Anda :")
                print("1. Sudah Selesai !")
                print("2. Belanja Lagi ?")
                self.ljtmenu()
                
        def ljtmenu(self):
            pilihan = int(input("Pilihan opsi belanja : "))
            if pilihan == 1:
                print("Pilihan berakhir")
            elif pilihan == 2:
                self.pilihblj()
                
            else:
                print("Pilihan belanja tidak ada :")
                self.ljtmenu()
                
        def getdfblj(self):
            for i in self.brg:
                print(i)
            print("Total harga Rp " + str(self.harga))
            
        def getkmblhrg(self):
            bayar = int(input("Masukkan uang belanja Anda : "))
            sisabayar = bayar - self.harga
            
            if bayar < self.harga:
                print("bayar belanja anda kurang !")
            elif bayar >= self.harga:
                print("Bayar belanja anda Rp" + str(sisabayar))
            
                
        def result(self):
            self.daftarhrg()
            self.pilihblj()
            self.getdfblj()
            self.getkmblhrg()
            
toko = tokoabc()
toko.result()
