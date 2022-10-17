
def Terbilang(bil):
    satuan = ['', 'satu', 'dua', 'tiga', 'empat',
              'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    n = int(bil)
    if (n >= 0 and n <= 11):
        return satuan[n]
    elif (n < 20):
        return Terbilang(n - 10) + " Belas "
    elif (n < 100):
        return Terbilang(n / 10) + ' Puluh ' + Terbilang(n % 10)
    else:
        return 'wrong input'


while(True):
    number = input('Masukkan Angka(0 - 99): ')
    if(int(number) == 0):
        print('nol')
    else:
        angka_terbilang = Terbilang(number)
        print(angka_terbilang)
