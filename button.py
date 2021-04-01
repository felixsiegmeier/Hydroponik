#Interrupt-Handler
# übergeben werden Pin und Zahl, bis  zu der gezählt wird
''' button = Button(17,5) erzeugt einen PULL_DOWN-Button auf Pin 17 mit Aktivierung auf Druck, 
der von 0 bis 5 aufwärts zählt und dann wieder bei 0 beginnt '''
from machine import Pin

class Button():
    def __init__(self, button_pin, counter_range):
        self.counter = 0 #gibt den Zähler wieder
        self.pin = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
        self.range = counter_range
        self.pin.irq(trigger=Pin.IRQ_RISING, handler=self.update_counter)
    
    def update_counter(self, arg):
        if self.counter < self.range:
            self.counter += 1
        else:
            self.counter = 0

    def value(self):
        return (self.counter)
