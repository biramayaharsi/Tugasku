def Main() : 
    print("="*70)
    print('{:^70}'.format("PARKIRAN LIPPO PLAZA"))
    print('{:^70}'.format("Jl. Gajah Mada 104 68131 Jember East Java"))
    print("="*70)
    print("Tipe Kendaraan \n 1. Untuk Mobil [M1] \t 2. Untuk Motor [M2]")
    tipe = input("Masukkan Tipe Kendaraan Anda : ")
    jamMasuk = int(input("Masukkan Jam Kedatangan : "))
    jamKeluar = int(input("Masukkan Jam Pulang : "))

    if tipe == "1" or tipe == "[M1]" or tipe == "M1" :
        lama_parkir = jamKeluar - jamMasuk
        biaya_parkir = lama_parkir * 5000
        print("="*50)
        print("Lama Parkir Mobil : ", lama_parkir, "jam")
        print("Biaya Parkir Mobil Rp. ", biaya_parkir)
        print("="*50)
    elif tipe == "2" or tipe == "[M2]" or tipe == "M2" :
        lama_parkir2 = jamKeluar - jamMasuk
        biaya_parkir2 = lama_parkir2 * 2000
        print("="*50)
        print("Lama Parkir Motor : ", lama_parkir2, "jam")
        print("Biaya Parkir Motor Rp. ", biaya_parkir2)
        print("="*50)
    else :
        Main()

Main()