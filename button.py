#Interrupt-Handler
''' Funktion, in die Pin und Range der Modi eingetragen werden => 4 bedeutet, dass von 0 bis 3 durchgewechselt wird
    Init ruft den Interrupthandler selbst auf für den Pin und mit der gewünschten Funktion auf dem Pin
    toggle beschreibt, ob es on_active oder on_release ist oder Toggleswitch ist 
    mode beschreibt, ob der Button PULLUP oder PULLDOWN sein soll'''

class InterruptButton():
    def __init__(self, button_pin, mode, toggle, action):
        self.counter = 0
    
    def counter(self, range):
        if self.count < range:
            self.counter += 1
        else:
            self.count = 0
