def posisi():
    f = open('input2.txt', 'r')
    for i in f:
        awal = i.split('/') # memisahkan input menjadi list
    
    hasil = []
    for i in awal:
        x = list(i)
        hasil.extend(x) # membuat list yang isinya hanya 1 karakter per elemen

    f.close()

    return hasil

def nilai_buah(a, b):
# parameter a untuk memasukan fungsi posisi()
# parameter b untuk memeriksa warna yang akan dihitung

    bidak = []
    nilai = 0

    for i in a:
        if b == "hitam":
            if i in ['k', 'q', 'r', 'b', 'n', 'p']:
                bidak.append(i)

        elif b == "putih":
            if i in ['K', 'Q', 'R', 'B', 'N', 'P']:
                bidak.append(i)

# perulangan untuk memeriksa bidak apa saja yang ada
# pengkondisian untuk menghitung nilai warna tersebut
    for c in bidak:
        if c in ['k', 'K']:
            nilai += 200
        if c in ['q', 'Q']:
            nilai += 9
        if c in ['r', 'R']:
            nilai += 5
        if c in ['b', 'n', 'B', 'N']:
            nilai += 3
        if c in ['p', 'P']:
            nilai += 1

    print("\nnilai",b + ":" ,nilai)

def jumlah_petak_kosong(a):
    kosong = []
    for i in a:
        
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            kosong.append(int(i))

    print("\njumlah petak kosong:",sum(kosong))


def main():
    posisi()
    print("posisi:",posisi())
    nilai_buah(posisi(), "hitam")
    nilai_buah(posisi(), "putih")
    jumlah_petak_kosong(posisi())

main()