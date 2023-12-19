print('\nKonversi Suhu Reamur')
print('='*20,'\n')

def cari_celsius(suhu):
    C = suhu * 5/4
    return C

def cari_fahrenheit(suhu):
    F = (suhu * 9/4) + 32
    return F

def cari_kelvin(suhu):
    K = (suhu * 5/4) + 273
    return K

suhu = float(input('Masukkan suhu dalam reamur: '))

C = cari_celsius(suhu)
F = cari_fahrenheit(suhu)
K = cari_kelvin(suhu)

print(f'Suhu dalam Reamur = {suhu}')
print(f'suhu dalam Celcius = {C} °Celcius')
print(f'suhu dalam Farenheit = {F} °Farenheit')
print(f'suhu dalam Kelvin = {K} °Kelvin')