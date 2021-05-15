from machine import Pin

class LichtController:
    def __init__(self, mosfet_gate_pin):
        self.mosfet_gate = Pin(mosfet_gate_pin, Pin.OUT)
        self.hour = 0
        self.mosfet_gate.value(0)

    def update_values(self, hour):
        self.hour = hour

    def licht _steuern(self,licht_modus,hour):
        self.update_values(hour)
        min = 5
        max = 13+2*licht_modus
        if hour > min and hour < max:
            self.mosfet_gate.value(1)
        else:
            self.mosfet_gate.value(0)