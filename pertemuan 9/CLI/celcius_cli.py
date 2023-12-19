print('\nKonversi Suhu Celcius')
print('='*20,'\n')

suhu = float(input('Masukkan suhu dalam celcius: ',))

F = (9/5 * suhu) + 32
R = (4/5 * suhu)
K = (suhu) +273

print(f'Suhu dalam Celcuis = {suhu}')
print(f'suhu dalam Farenheit = {F} °Farenheit')
print(f'suhu dalam Reamur = {R} °Reamus')
print(f'suhu dalam Kelvin = {K} °Kelvin')