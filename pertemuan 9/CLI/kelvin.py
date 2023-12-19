print('\nKonversi Suhu Kelvin')
print('='*20,'\n')

def cari_celsius(suhu):
    C = (suhu - 273)
    return C

def cari_reamur(suhu):
    R = (suhu - 273) * 4/5
    return R

def cari_farenheit(suhu):
    F = ((suhu - 273) * 9/5) + 32
    return F

suhu = float(input('Masukkan suhu dalam Kelvin: '))

C = cari_celsius(suhu)
R = cari_reamur(suhu)
F = cari_farenheit(suhu)

print(f'Suhu dalam Kelvin = {suhu}')
print(f'suhu dalam Celcius = {C} °Celcius')
print(f'suhu dalam Reamur = {R} °Reamur')
print(f'suhu dalam Farenheit = {F} °Farenheit')