from temperatursensoren import TempSensor
from button import Button
from ecsensor import EcSensor
import uhrzeit
import time

class Daten:
    def __init__(self):
        self.tempsensor = TempSensor(19)
        self.buttons = Button(17,33,4,5,4)
        self.ec = EcSensor(26,34,2000,4095,5)
        self.prev_sekunde = time.time()
        self.prev_5_minuten = time.time()

        self.temp_tank = self.tempsensor.get_temp(0)
        self.temp_rohr = self.tempsensor.get_temp(1)
        self.ec_value = self.ec.get_ec(self.temp_tank)
        self.uhrzeit = []
        self.hour = 0
        self.minute = 0
        self.licht_modus = self.buttons.get_licht_modus()
        self.oled_modus = self.buttons.get_oled_modus()
    
    def update_sekundlich(self):
        if time.time() - self.prev_sekunde > 0:
            self.prev_sekunde = time.time()
            return True
        else:
            return False
    
    def update_5_minutlich(self):
        if time.time() - self.prev_5_minuten > 300:
            self.prev_5_minuten = time.time()
            return True
        else:
            return False
    
    def update_values(self):
        if self.update_5_minutlich() == True:
            try:
                self.temp_tank = self.tempsensor.get_temp(0)
                self.temp_rohr = self.tempsensor.get_temp(1)
                self.ec_value = self.ec.get_ec(self.temp_tank)
            except: pass
        if self.update_sekundlich() == True:
            try:
                uhrzeit.uhrzeitloop()
                self.uhrzeit = uhrzeit.get_time()
                self.hour = uhrzeit.get_hour()
                self.minute = uhrzeit.get_minute()
            except: pass
        self.licht_modus = self.buttons.get_licht_modus()
        self.oled_modus = self.buttons.get_oled_modus()
    
    def get_value(self, wert):
        if wert == "temp_tank":
            return self.temp_tank
        if wert == "temp_rohr":
            return self.temp_rohr
        if wert == "ec":
            return self.ec_value
        if wert == "hour":
            return self.hour
        if wert == "minute":
            return self.minute
        if wert == "zeit":
            return self.uhrzeit
        if wert == "licht_modus":
            return self.licht_modus
        if wert == "oled_modus":
            return self.oled_modus
    
    def get_oled_payload(self):
        oled_payload = [False,[self.get_value("temp_tank"),self.get_value("temp_rohr")],self.get_value("ec"),self.get_value("zeit"), self.get_value("licht_modus")]
        return (oled_payload[self.get_value("oled_modus")])