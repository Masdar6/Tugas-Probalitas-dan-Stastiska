# Nama : Masdar
# Nim : D0221323
# kelas : Informatika E


list_nim = [0, 2, 2, 1, 3, 2, 3]

def rata_rata (deret):
    return sum(deret) / len(deret)
print(f'data = {list_nim}')
print(f'nilai mean = {rata_rata(list_nim)}')
def nilai_tengah(deret):
    deret.sort()
    n = len(deret)
    i_tengah = n // 2

    if n % 2 == 1:
        return deret[i_tengah]

        return (deret[i_tengah - 1] + deret[i_tengah]) /2
print(f'data = {list_nim}')
print(f'nilai median = {nilai_tengah(list_nim)}')

def nilai_terbanyak(deret):
    peta_kemunculan = {}

    for bilangan in deret:
        if bilangan in peta_kemunculan:
            peta_kemunculan[bilangan]+=1
        else:
            peta_kemunculan[bilangan] =1
    bilangan_terbesar = deret[0]
    for bilangan in peta_kemunculan.keys():
        jumlah = peta_kemunculan[bilangan]

        if jumlah>peta_kemunculan[bilangan_terbesar]:
            bilangan_terbesar = bilangan

    return bilangan_terbesar

inputan = input('masukkan data nim anda:')#pisahkan dengan koma setiap data nim anda!
data = [] #contoh data nim saya = 0, 2, 2, 1, 3, 2, 3
for bilangan in inputan.split(','):
    data.append(int(bilangan))

print(f'data = {list_nim}')
print(f'nilai modus = {nilai_terbanyak(list_nim)}')

#Output
# data = [0, 2, 2, 1, 3, 2, 3]
# nilai mean = 1.8571428571428572
# data = [0, 2, 2, 1, 3, 2, 3]
# nilai median = 2
# masukkan data nim anda:0,2,2,1,3,2,3 
# data = [0, 1, 2, 2, 2, 3, 3]
# nilai modus = 2