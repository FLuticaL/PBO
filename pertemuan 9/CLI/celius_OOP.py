print('\nKonversi Suhu Celcius')
print('='*20,'\n')

class Celcius:
    def __init__(self,suhu):
        self.suhu = suhu
        
    def cari_celcius(self):
        val = self.suhu
        return val
                
    def cari_farenheit(self):
        val = (9/5 * self.suhu) + 32
        return val

    def cari_reamur(self):
        val = (4/5 * self.suhu)
        return val

    def cari_kelvin(self):
        val = (self.suhu) +273
        return val

suhu = float(input('Masukkan suhu dalam celcius: '))
C = Celcius(suhu)
val = C.cari_celcius()

F = C.cari_farenheit()
R = C.cari_reamur()
K = C.cari_kelvin()

print(f'Suhu dalam Celcuis = {suhu}')
print(f'suhu dalam Farenheit = {F} °Farenheit')
print(f'suhu dalam Reamur = {R} °Reamus')
print(f'suhu dalam Kelvin = {K} °Kelvin')