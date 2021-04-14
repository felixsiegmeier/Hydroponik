from machine import Pin

class PumpenController:
    def __init__(self, mosfet_gate_pin, minute, temp):
        mosfet_gate = Pin(mosfet_gate_pin, Pin.OUT)
        self.minute = minute
        self.temp = temp
        mosfet_gate.value(0)
        while True:
            if self.minute < 6:
                mosfet_gate.value(1)
                return
            elif abs(self.temp[0]-self.temp[1]) > 5:
                    mosfet_gate.value(1)
            else:
                mosfet_gate.value(0)

    def update(self, minute, temp):
        self.minute = minute
        self.temp = temp