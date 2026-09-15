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
    print("1. tampilkan data buku")
    print("2. tampilkan data penerbit")
    print("3. hapus data penerbit")
    print("4. update data penulis")
    print("5. keluar")
    
    pilihan = input("pilih menu (1-5): ")

#Tampilkan data buku ketika pengguna memilih menu tampilkan data
    if pilihan == "1":
        print(buku["data_buku"])

    elif pilihan == "2":
        print(buku["data_penerbit"])

    elif pilihan == "3":
        del buku["data_penerbit"]

        print("Setelah Delete:")
        print(buku)

    elif pilihan == "4":
        update = input("ubah nama penulis:")
        buku["data_buku"].update({"penulis" : {update}})

        print("Setelah Update:")
        print(buku)

    elif pilihan == "5":
        print("anda keluar")
        break