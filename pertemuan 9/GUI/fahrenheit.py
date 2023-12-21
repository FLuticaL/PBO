class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu    
        
    def get_fahrenheit(self):
        val = self.suhu
        return val
    
    def get_celcius(self): 
        val = (self.suhu - 32) * 5/9
        return val
    
    def get_reamur(self): 
        val = (self.suhu - 32) * 4/9
        return val
    
    def get_kelvin(self): 
        val = ((self.suhu - 32) * 5/9) + 273
        return val        