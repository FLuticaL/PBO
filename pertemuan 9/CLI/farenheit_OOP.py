print('\nKonversi Suhu Farenheit')
print('='*20,'\n')

class Farenheit:
    def __init__(self,suhu):
        self.suhu = suhu
        
    def cari_farenheit(self):
        val = self.suhu
        return val
                
    def cari_celcius(self):
        val = (self.suhu - 32) * 5/9
        return val

    def cari_reamur(self):
        val = (self.suhu - 32) * 4/9
        return val

    def cari_kelvin(self):
        val = ((self.suhu - 32) * 5/9) + 273
        return val

suhu = float(input('Masukkan suhu dalam Farenheit: '))
F = Farenheit(suhu)
val = F.cari_farenheit()

C = F.cari_celcius()
R = F.cari_reamur()
K = F.cari_kelvin()

print(f'Suhu dalam Farenheit = {suhu}')
print(f'suhu dalam Celcius = {C} Celcius')
print(f'suhu dalam Reamur = {R} °Reamus')
print(f'suhu dalam Kelvin = {K} °Kelvin')