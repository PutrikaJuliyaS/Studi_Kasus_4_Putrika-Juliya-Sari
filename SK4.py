#DATA BUKU
buku = {
    "data_buku" :{
    "judul" : "harry potter",
    "penulis" : "j.k. rowling",
    "tahun_terbit" : "1997"
    },
#Tambahkan data penerbit ke dalam Dictionary
    "data_penerbit" :{
    "penerbit" : "bloomsbury publishing",
    "negara" : "britania raya"
    }
}

#perulangan untuk menampilkan menu
while True:
    print("1. tampilkan data buku dan penerbit")
    print("2. tampilkan data buku")
    print("3. tampilkan data penerbit")
    print("4. hapus data penerbit")
    print("5. keluar")
    
    pilihan = input("pilih menu (1-5): ")

#Tampilkan data buku ketika pengguna memilih menu tampilkan data
    if pilihan == "1":
        print(buku)

    elif pilihan == "2":
        print(buku["data_buku"])

    elif pilihan == "3":
        print(buku["data_penerbit"])

    elif pilihan == "4":
        del buku["data_penerbit"]

        print("Setelah Delete:")
        print(buku)

    elif pilihan == "5":
        print("anda keluar")
        break

#Ubah data penulis pada Dictionary
buku["data_buku"].update({"penulis": "joanne rowling"})

print("Setelah Update:")
print(buku)