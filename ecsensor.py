from machine import Pin, ADC
from time import sleep

class EcSensor():
    def __init__(self, power, data, resistor, analog_range, konst):
        self.ec_power = Pin(power, Pin.OUT) #Pin, der den Sensor aktiviert (also den MOSFET steuert)
        self.ec_power.value(0)
        self.ec_data = ADC(Pin(data)) #Analoger Eingangspin
        self.ec_data.atten(ADC.ATTN_11DB)
        self.resistor = resistor #Widerstand des Spannungsteilers => 2k funktioniert gut
        self.konst = konst #Sensorkonstante, ggf. experimentell oder per Funktion ermitteln
        if self.konst <= 0:
            print("Die Sensorkonstante muss festgelegt werden.")
            print("Führe get_konst(temp, ec_bekannt) mit einer bekannten Lösung aus, um diese zu bestimmen.")
        self.pin_resistance = 25 #Eingangswiderstand des Microkontrollers
        self.range = analog_range #4095 für ESP32, 1023 für ESP8266

    def get_ec(self,temp):
        self.ec_power.value(1)
        raw = self.ec_data.read()
        raw = self.ec_data.read()
        self.ec_power.value(0)
        sleep(1)
        v_drop = self.voltage*raw/self.range
        resistance = (v_drop * self.resistor) / (self.voltage - v_drop)
        resistance = resistance - self.pin_resistance
        ec_value = 1000/(resistance*self.konst)
        ec_value_25 = 1000*ec_value/(1+0.019*(temp-25.0))
        return(ec_value_25)
    
    def get_konst(self, temp, ec_bekannt):
        buffer = 0
        for i in range(10):
            self.ec_power.value(1)
            raw = self.ec_data.read()
            raw = self.ec_data.read()
            print("Messwert",str(i),"von 10:",str(raw))
            buffer += raw
            self.ec_power.value(0)
            sleep(1)
        avg = buffer/10
        v_drop = self.voltage*avg/self.range
        resistance = (v_drop * self.resistor) / (self.voltage - v_drop)
        resistance = resistance - self.pin_resistance
        ec_no_temp = ec_bekannt*(1+(0.019*(temp-25.0)))
        konst = 1000/(resistance*ec_no_temp) # eventuell muss hier 1/ statt 1000/ hin, weil ich mit µS/cm und nicht mit S/cm rechte... probieren
        print("Die Sensorkonstante",str(konst),"wurde gespeichert")
        self.konst = konst
