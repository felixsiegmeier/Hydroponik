from machine import Pin
import time

class Button():
    def __init__(self, oled_button_pin, licht_button_pin, oled_modus_counter_max, licht_modus_counter_max, oled_modus_licht):
        self.oled_modus_counter = 0
        self.licht_modus_counter = 0
        self.button_zuletzt_getrueckt = time.time()
        self.oled_pin = Pin(oled_button_pin, Pin.IN, Pin.PULL_DOWN)
        self.licht_pin = Pin(licht_button_pin, Pin.IN, Pin.PULL_DOWN)
        self.oled_modus_counter_max = oled_modus_counter_max
        self.licht_modus_counter_max = licht_modus_counter_max
        self.oled_modus_licht = oled_modus_licht
        self.oled_pin.irq(trigger=Pin.IRQ_RISING, handler=self.oled_handler)
        self.licht_pin.irq(trigger=Pin.IRQ_RISING, handler=self.licht_handler)
#        while True:
#            if time.time() - self.button_zuletzt_getrueckt > 180:
#                self.oled_modus_counter = 0
    
    def oled_handler(self, arg):
        self.button_zuletzt_getrueckt = time.time()
        if self.oled_modus_counter < self.oled_modus_counter_max:
            self.oled_modus_counter += 1
        else:
            self.oled_modus_counter = 0
        print("oled_modus_counter:",self.oled_modus_counter)

    def licht_handler(self, arg):
        self.button_zuletzt_getrueckt = time.time()
        self.oled_modus_counter = self.oled_modus_licht
        if self.licht_modus_counter < self.licht_modus_counter_max:
            self.licht_modus_counter += 1
        else:
            self.licht_modus_counter = 0
        print("licht_modus_counter:",self.licht_modus_counter)

    def get_oled_modus(self):
        return (self.oled_modus_counter)

    def get_licht_modus(self):
        return (self.licht_modus_counter)