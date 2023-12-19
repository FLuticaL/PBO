print('\nKonversi Suhu Kelvin')
print('='*20,'\n')

class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def cari_kelvin(self):
        val = self.suhu
        return val

    def cari_celsius(self):
        val = (self.suhu - 273)
        return val

    def cari_reamur(self):
        val = (self.suhu - 273) * 4/5
        return val

    def cari_farenheit(self):
        val = ((self.suhu - 273) * 9/5) + 32
        return val    

suhu = float(input('Masukkan suhu dalam kelvin: '))
K = Kelvin(suhu)

C = K.cari_celsius()
R = K.cari_reamur()
F = K.cari_farenheit()

print(f'Suhu dalam Kelvin = {suhu}')
print(f'suhu dalam Celcius = {C} °Celcius')
print(f'suhu dalam Reamur = {R} °Reamur')
print(f'suhu dalam Farenheit = {F} °Farenheit')