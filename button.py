from machine import Pin

class Button():
    def __init__(self, oled_button_pin, licht_button_pin, oled_modus_counter_max, licht_modus_counter_max, oled_modus_licht):
        self.oled_modus_counter = 0
        self.licht_modus_counter = 0 
        self.oled_pin = Pin(oled_button_pin, Pin.IN, Pin.PULL_DOWN)
        self.licht_pin = Pin(licht_button_pin, Pin.IN, Pin.PULL_DOWN)
        self.oled_modus_counter_max = oled_modus_counter_max
        self.licht_modus_counter_max = licht_modus_counter_max
        self.oled_modus_licht = oled_modus_licht
        self.oled_pin.irq(trigger=Pin.IRQ_RISING, handler=self.oled_handler)
        self.licht_pin.irq(trigger=Pin.IRQ_RISING, handler=self.licht_handler)
    
    def oled_handler(self, arg):
        if self.oled_modus_counter < self.oled_modus_counter_max:
            self.oled_modus_counter += 1
        else:
            self.oled_modus_counter = 0

    def licht_handler(self, arg):
        self.oled_modus_counter = self.oled_modus_licht
        if self.licht_modus_counter < self.licht_modus_counter_max:
            self.licht_modus_counter += 1
        else:
            self.licht_modus_counter = 0

    def get_oled_modus(self):
        return (self.oled_modus_counter)

    def get_licht_modus(self):
        return (self.licht_modus_counter)