print('\nKonversi Suhu Farenheit')
print('='*20,'\n')

suhu = float(input('Masukkan suhu dalam Farenheit: '))

C = (suhu - 32) * 5/9
R = (suhu - 32) * 4/9
K = ((suhu - 32) * 5/9) + 273

print(f'Suhu dalam Farenheit = {suhu}')
print(f'suhu dalam Celcius = {C} Celcius')
print(f'suhu dalam Reamur = {R} °Reamus')
print(f'suhu dalam Kelvin = {K} °Kelvin')