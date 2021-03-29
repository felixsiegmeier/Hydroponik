#Interrupt-Handler
''' Funktion, in die Pin und Range der Modi eingetragen werden => 4 bedeutet, dass von 0 bis 3 durchgewechselt wird
    Init ruft den Interrupthandler selbst auf für den Pin und mit der gewünschten Funktion auf dem Pin
    toggle beschreibt, ob es push oder release ist
    mode beschreibt, ob der Button PULLUP oder PULLDOWN sein soll'''

class InterruptButton():
    def __init__(self, button_pin, mode, toggle, action):
        self.counter = 0
        if mode == "pullup":
            self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
        if mode == "pulldown":
            self.button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
        if toggle == "push":
            self.button.irq(trigger=Pin.IRQ_RISING, handler=action)
        if toggle == "release":
            self.button.irq(trigger=Pin.IRQ_FALLING, handler=action)
    
    def counter(self, range):
        if self.count < range:
            self.counter += 1
        else:
            self.count = 0
