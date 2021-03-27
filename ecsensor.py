from machine import Pin, ADC

class EcSensor():
    def __init__(self, power, data, resistor, temp, controller, max, min):
        self.ec_power = Pin(power, Pin.OUT)
        self.ec_power.value(0)
        self.ec_data = ADC(Pin(data))
        self.ec_data.atten(ADC.ATTN_11DB)
        self.resistor = resistor
        self.temp = temp
        self.r_max = max
        self.r_min = min
        if controller == "ESP32":
            self.pin_resistance = 25
            self.range = 4095
            self.voltage = 3.3
        if Controller == "ESP8266":
            self.pin_resistance = 25
            self.range = 1023
            self.voltage = 3.3

    def ec_measure(self):
        raw = self.ec_data.read()
        v_drop = self.voltage*self.raw/self.range
        Resistance = (v_drop * self.resistor) / (self.voltage - v_drop)
        resistance = resistance - self.pin_resistance
        resistance_25 = resistance/(1+(0.019*(self.temp-25)))




