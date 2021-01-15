print("Selamat Datang di ATM Saya")
print("Pilih Option yang anda inginkan")
print("1. Cek Tabungan")
print("2. Ambil Uang saya")
print("3. Tabung Uang saya")
option = int(input("Silakan pilihh option: "))
if option == 1:
    print("Uang kamu berjumlah 100.000")
elif option == 2:
    print("Unang kamu berjumlah 200.000, Mau ambil berapa? ")
    print("1. 100.000")
    print("2. 200.000")
    uang_kamu =200000
    option2 = int(input("Masukan option: "))
    if option2 == 1:
        hasil = uang_kamu - 100000
        print("Uang kamu sekarang berjumlah", hasil)
    elif option2 == 2:
        hasil2 = uang_kamu - 200000
        print("Uang kamu sekarang berjumlah", hasil2)
    else:
        print("Keyword Anda salah")
elif option == 3:
    uang_kamu = 200000
    print("Mau menabyng berapa cuy")
    option3 = int(input("Masukan Jumlah ung yang kan di tabung: "))
    hasil3 = uang_kamu + option3
    print("Jumlah uang kamu sekrang dalah", hasil3)
else:
    print("Keword anda salah, silakan coba lagi")

