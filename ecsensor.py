from machine import Pin, ADC

class EcSensor:
    def __init__(self, pin):
        self.ec_data = ADC(Pin(pin)) #Analoger Eingangspin
        self.ec_data.atten(ADC.ATTN_11DB)
    
    def get_raw(self):
        return self.ec_data.read()
    
    def get_voltage(self):
        vin = 3.3
        analog_range = 4095
        volt = self.get_raw()*vin/analog_range
        return volt
    
    def get_voltage_temp(self, temp):
        temp_coef = 1+0.02*(temp-25)
        volt = self.get_voltage()/temp_coef
        return volt

    def get_tds(self, temp):
        volt = self.get_voltage_temp(temp)
        tds = (133.42*volt*volt+volt-255.86*volt*volt+857.39*volt)*0.5
        return round(tds,1)


