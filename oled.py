from ssd1306 import SSD1306_I2C
from machine import Pin, I2C

class Oled():
    def __init__(self, sda_pin, scl_pin):
        self.oled = SSD1306_I2C(128, 64, I2C(scl=Pin(scl_pin), sda=Pin(sda_pin)))
    
    def show_off(self, payload):
        #payload = None
        pass

    def show_temp(self, payload):
        #payload = list
        pass

    def show_ec(self, payload):
        #payload = int
        pass

    def show_time(self, payload):
        #payload = str(?)
        pass
    
    def show_light(self, payload):
        #payload = int = button.licht_modus_counter
        pass

    def oled_display(self, **kwargs):
        oled_modus_auswahl = [self.show_off, self.show_temp, self.show_ec, self.show_time, self.show_light]
        oled_modus_counter = kwargs.get("OLED_MODUS_COUNTER")
        payload = kwargs.get("PAYLOAD", None)
        oled_modus_auswahl[oled_modus_counter](payload)
