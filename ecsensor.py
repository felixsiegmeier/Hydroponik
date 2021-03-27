from machine import Pin, ADC

class ecsensor():
    def __init__(self, Power, GND, Data, R, Temp, Controller, max, min):
        self.ECPower = Pin(Power, Pin.OUT)
        self.ECPower.value(0)
        self.ECGND.value(0)
        self.ECGND = Pin(GND, Pin.OUT)
        self.ECData = ADC(Pin(Data))
        self.ECData.atten(ADC.ATTN_11DB)
        self.Resistor = R
        self.Temp = Temp
        self.Rmax = max
        self.Rmin = min
        if Controller == "ESP32":
            self.Rc = 25
            self.range = 4095
            self.voltage = 3.3
        if Controller == "ESP8266":
            self.Rc = 25
            self.range = 1023
            self.voltage = 3.3

    def measureEC(self):
        raw = self.ECData.read()
        Vdrop = self.voltage*self.raw/self.range
        Resistance = (Vdrop * self.Resistor) / (self.voltage - Vdrop)
        Resistance = Resistance - self.Rc
        Resistance25 = Resistance/(1+(0.019*(self.Temp-25)))




