#Interrupt-Handler
''' Funktion, in die Pin und Range der Modi eingetragen werden => 4 bedeutet, dass von 0 bis 3 durchgewechselt wird
    Init ruft den Interrupthandler selbst auf für den Pin und mit der gewünschten Funktion auf dem Pin
    toggle beschreibt, ob es push oder release ist
    mode beschreibt, ob der Button PULLUP oder PULLDOWN sein soll'''

from machine import Pin

class Button():
    def __init__(self, button_pin, counter_range):
        self.counter = 0
        self.pin = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
        self.range = counter_range
        self.pin.irq(trigger=Pin.IRQ_RISING, handler=self.update_counter)
    
    def update_counter(self, arg):
        if self.counter < self.range:
            self.counter += 1
        else:
            self.counter = 0
