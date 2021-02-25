# aplikasi mini_kasir
# nama file : mini-kasir.py
class tokomuda():
    data = [{"nmbrg": "Tissue", "harga": 4000},
              {"nmbrg": "Minyak", "harga": 3000},
              {"nmbrg": "Telur", "harga": 25000},
              {"nmbrg": "Keju", "harga": 15000},
              {"nmbrg": "Tepung", "harga": 25000},
              {"nmbrg": "Beras", "harga": 13500},
              {"nmbrg": "Mie", "harga": 3000},
              {"nmbrg": "Gula", "harga": 8500}
             ]
    
nama = input("Masukan nama pelanggan : ")
tanggal = input("Masukan tanggal pembelian : ")

print("         ==== MENU ====")
print("1. Tissue             Rp 4000")
print("2. Minyak            Rp 30000")
print("3. Telur             Rp 25000")
print("4. Keju              Rp 15000")
print("5. Tepung            Rp 25000")
print("6. Beras             Rp 13500")
print("7. Mie               Rp 3000")
print("8. Gula              Rp 8500")
print("         ==== MENU ====")

menu_pesanan = int(input("Masukan menu pesanan (Nomer Menu) : "))

if menu_pesanan == 1:
    harga = 6000
elif menu_pesanan == 2:
    harga = 30000
elif menu_pesanan ==3:
    harga = 25000
elif menu_pesanan == 4:
    harga = 15000
elif menu_pesanan == 5:
    harga = 25000
elif menu_pesanan == 6 :
    harga = 13500
elif menu_pesanan == 7 :
    harga = 3000
elif menu_pesanan == 8 :
    harga = 8500
else :    
    while True:
        print("=====Menu Tidak Tersedia,Silahkan Pilih Menu Lainnya!!=====")
        menu_pesanan = int(input("Masukan menu pesanan (Nomer Menu) : "))
    if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan == 3 or menu_pesanan == 4 or menu_pesanan == 5 or menu_pesanan == 6 or menu_pesanan == 7 or menu_pesanan == 8:
        
        if menu_pesanan == 1:
            harga = 6000
        elif menu_pesanan == 2:
            harga = 30000
        elif menu_pesanan == 3:
            harga = 25000
        elif menu_pesanan == 4:
            harga = 15000
        elif menu_pesanan == 5:
            harga = 25000
        elif menu_pesanan == 6:
            harga = 13500
        elif menu_pesanan == 7:
            harga = 3000
        elif menu_pesanan == 8:
            harga = 8500
        
jumlah_pembelian = int(input("Masukan Jumlah Pembelian : "))
bayar = jumlah_pembelian * harga

print("Anda Harus Membayar : Rp.{}".format(bayar))
