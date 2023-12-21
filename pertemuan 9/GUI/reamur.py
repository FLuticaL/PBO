class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_celcius(self):
        val = (self.suhu * 5/4)
        return val
    
    def get_fahrenheit(self):
        val = (9/4 * self.suhu) + 32
        return val    

    def get_kelvin(self):
        val = (self.suhu * 5/4) + 273
        return val        