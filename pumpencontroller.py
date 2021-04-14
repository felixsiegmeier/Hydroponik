from machine import Pin

class PumpenController:
    def __init__(self, mosfet_gate_pin):
        self.mosfet_gate = Pin(mosfet_gate_pin, Pin.OUT)
        self.minute = 0
        self.temp = 0
        self.mosfet_gate.value(0)

    def update_values(self, minute, temp):
        self.minute = minute
        self.temp = temp

    def pumpe_steuern(self,dauer,minute,temp):
        self.update_values(minute, temp)
        if self.minute < dauer:
            self.mosfet_gate.value(1)
        elif abs(self.temp[0]-self.temp[1]) > 5:
            self.mosfet_gate.value(1)
        else:
            self.mosfet_gate.value(0)       
