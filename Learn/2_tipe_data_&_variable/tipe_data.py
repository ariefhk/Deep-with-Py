

def angkaTerbilang(angka):
    satuan = ['', 'satu', 'dua', 'tiga', 'empat',
              'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
    if(angka < 0):
        return 'negatif' + angkaTerbilang(-1)
    elif(angka < 10):
        return satuan[angka]
    elif(angka < 100):
        # return satuan[int((angka-(angka % 10))/10)] + ' puluh ' + angkaTerbilang(angka % 10)
        return angkaTerbilang(angka - 10) + ' puluh ' + angkaTerbilang(angka % 10)
    elif(angka < 200):
        return satuan[int((angka - (angka % 100))/100)] + ' ratus ' + angkaTerbilang(angka % 100)


print(angkaTerbilang(-2))
# print((120 - (120 % 100))/100)
