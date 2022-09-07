
satuan = ['', 'satu', 'dua', 'tiga', 'empat',
              'lima', 'enam', 'tujuh', 'delapan', 'sembilan']


def angkaTerbilang(angka):
    if(angka < 0):
        return 'negatif' + angkaTerbilang(-1)
    elif(angka < 10):
        return satuan[angka]
    elif(angka < 100):
        return satuan[int((angka-(angka % 10))/10)] + ' puluh ' + angkaTerbilang(angka % 10)
    elif(angka < 200):
        return satuan[int((angka - (angka % 100))/100)] + ' ratus ' + angkaTerbilang(angka % 100)


print(angkaTerbilang(120))
# print((120 - (120 % 100))/100)
