print('\nKonversi Suhu Kelvin')
print('='*20,'\n')

suhu = float(input('Masukkan suhu dalam Kelvin: '))

C = (suhu - 273)
R = (suhu - 273) * 4/5
F = ((suhu - 273) * 9/5) + 32

print(f'Suhu dalam Kelvin = {suhu}')
print(f'suhu dalam Celcius = {C} °Celcius')
print(f'suhu dalam Reamur = {R} °Reamur')
print(f'suhu dalam Farenheit = {F} °Farenheit')