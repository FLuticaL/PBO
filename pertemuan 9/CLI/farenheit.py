print('\nKonversi Suhu Farenheit')
print('='*20,'\n')

def cari_celcius(suhu):
    C = (suhu - 32) * 5/9
    return C

def cari_reamur(suhu):
    R = (suhu - 32) * 4/9
    return R

def cari_kelvin(suhu):
    K = ((suhu - 32) * 5/9) + 273
    return K

suhu = float(input('Masukkan suhu dalam Farenheit: '))

C = cari_celcius(suhu)
R = cari_reamur(suhu)
K = cari_kelvin(suhu)

print(f'Suhu dalam Farenheit = {suhu}')
print(f'suhu dalam Celcius = {C} Celcius')
print(f'suhu dalam Reamur = {R} °Reamus')
print(f'suhu dalam Kelvin = {K} °Kelvin')