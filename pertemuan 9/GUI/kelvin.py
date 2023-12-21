class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu
        
    def get_kelvin(self):
        val = self.suhu
        return val

    def get_celcius(self):
        val = (self.suhu - 273)
        return val

    def get_reamur(self):
        val = (self.suhu - 273) * 4/5
        return val
        
    def get_fahrenheit(self):
        val = ((self.suhu - 273) * 9/5) + 32
        return val    