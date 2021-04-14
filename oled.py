from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

class Oled:
    def __init__(self, sda_pin, scl_pin):
        self.oled = SSD1306_I2C(128, 64, I2C(scl=Pin(scl_pin), sda=Pin(sda_pin)))
    
    def show_off(self, payload):
        #payload = None
        self.oled.poweroff()

    def show_temp(self, payload):
        #payload = list
        try:
            self.oled.poweron()
            self.oled.fill(0)
            self.oled.text("Temperaturen: ", 0, 5)
            self.oled.text("Tank: " + str(round(payload[0], 1)) + " C", 0, 25)
            self.oled.text("Rohr: " + str(round(payload[1], 1)) + " C", 0, 45)
            self.oled.show()
        except: pass

    def show_ec(self, payload):
        #payload = int
        try:
            maximum = 6000 # muss ggf. noch angepasst werden
            self.oled.poweron()
            self.oled.fill(0)
            self.oled.text("EC-Wert aktuell: ", 0, 5)
            self.oled.text(str(payload) + " yS/cm", 0, 25)
            self.oled.text(str(round(100*payload/maximum)) + " %", 0, 45)
            self.oled.show()
        except: pass

    def show_time(self, payload):
        #payload = liste mit 2 str
        try:
            self.oled.poweron()
            self.oled.fill(0)
            self.oled.text("Aktuelle Zeit: ", 0, 5)
            self.oled.text(payload[0], 0, 25)
            self.oled.text(payload[1], 0, 45)
            self.oled.show()
        except: pass
    
    def show_light(self, payload):
        #payload = int = button.licht_modus_counter
        try:
            self.oled.poweron()
            self.oled.fill(0)
            self.oled.text("Lichtstunden: "+str(8+payload*2), 0, 5)
            self.oled.text("Von "+str(5)+":00 Uhr", 0, 25)
            self.oled.text("Bis "+str(13+2*payload)+":00 Uhr", 0, 45)
            self.oled.show()
        except: pass

    def oled_display(self, **kwargs):
        oled_modus_auswahl = [self.show_off, self.show_temp, self.show_ec, self.show_time, self.show_light]
        oled_modus_counter = kwargs.get("OLED_MODUS_COUNTER")
        payload = kwargs.get("PAYLOAD", None)
        oled_modus_auswahl[oled_modus_counter](payload)
