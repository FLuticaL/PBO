print('\nKonversi Suhu Reamur')
print('='*20,'\n')

class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def cari_reamur(self):
        val = self.suhu
        return val

    def cari_celsius(self):
        val = self.suhu * 5/4
        return val
                
    def cari_fahrenheit(self):
        val = (self.suhu * 9/4) + 32
        return val

    def cari_kelvin(self):
        val = (self.suhu * 5/4) + 273
        return val

suhu = float(input('Masukkan suhu dalam reamur: '))
R = Reamur(suhu)

C = R.cari_celsius()
F = R.cari_fahrenheit()
K = R.cari_kelvin()

print(f'Suhu dalam Reamur = {suhu}')
print(f'suhu dalam Celcius = {C} °Celcius')
print(f'suhu dalam Farenheit = {F} °Farenheit')
print(f'suhu dalam Kelvin = {K} °Kelvin')