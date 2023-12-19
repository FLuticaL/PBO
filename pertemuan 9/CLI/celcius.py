print('\nKonversi Suhu Celcius')
print('='*20,'\n')

def cari_farenheit(suhu):
    F = (9/5 * suhu) + 32
    return F

def cari_reamur(suhu):
    R = (4/5 * suhu)
    return R

def cari_kelvin(suhu):
    K = (suhu) +273
    return K

suhu = float(input('Masukkan suhu dalam celcius: '))

F = cari_farenheit(suhu)
R = cari_reamur(suhu)
K = cari_kelvin(suhu)

print(f'Suhu dalam Celcuis = {suhu}')
print(f'suhu dalam Farenheit = {F} °Farenheit')
print(f'suhu dalam Reamur = {R} °Reamus')
print(f'suhu dalam Kelvin = {K} °Kelvin')