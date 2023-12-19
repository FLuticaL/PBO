print('\nKonversi Suhu Reamur')
print('='*20,'\n')

suhu = float(input('Masukkan suhu dalam Reamur: '))

C = (suhu * 5/4)
F = (suhu * 9/4) + 32
K = (suhu * 5/4) + 273

print(f'Suhu dalam Reamur = {suhu}')
print(f'suhu dalam Celcius = {C} °Celcius')
print(f'suhu dalam Farenheit = {F} °Farenheit')
print(f'suhu dalam Kelvin = {K} °Kelvin')