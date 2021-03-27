from machine import Pin, ADC

class ecsensor():
    def __init__(self, Power, GND, Data, R, Temp):
        self.ECPower = Pin(Power, Pin.OUT)
        self.ECPower.value(0)
        self.ECGND.value(0)
        self.ECGND = Pin(GND, Pin.OUT)
        self.ECData = ADC(Pin(Data))
        self.ECData.atten(ADC.ATTN_11DB)
