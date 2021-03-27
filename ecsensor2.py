from machine import Pin, ADC

class ecsensor():
    def __init__(self,R,Vin,K,ECground, ECpower, ECRead):
        self.R1 = R
        self.Ra = 25
        self.ECPin = ADC(Pin(ECRead))
        self.ECPin.atten(ADC.ATTN_11DB)
        self.ECGround = Pin(ECground, Pin.OUT)
        self.ECPower = Pin(ECpower, Pin.OUT)
        self.temp = 10
        self.EC = 0
        self.EC25 = 0
        self.raw = 0
        self.Vin = Vin
        self.Vdrop = 0
        self.Rc = 0
        self.TemperatureCoef = 0.019
        self.K = K
        
        self.ECGround.value(0)
        self.ECPower.value(0)

    def getec(self, temp):
        self.ECPower.value(1)
        self.raw = self.ECPin.read()
        self.raw = self.ECPin.read()
        self.ECPower.value(0)
        self.Vdrop = (self.Vin*self.raw)/4095
        self.Rc=(self.Vdrop*self.R1)/(self.Vin-self.Vdrop)
        self.Rc=self.Rc-self.Ra
        self.EC = 1000/(self.Rc*self.K)
        self.EC25 = 1000*self.EC/(1+ self.TemperatureCoef*(temp-25.0))
        return (self.EC25)

ec = ecsensor(2000,3.3,1,25,26,34)
print(str(ec.getec(19))+" "+str(ec.raw)) 

''' Hier wird bei einem Kurzschluss über den Messfühler (also über den Stecker) der MessPin auf GND gezogen = es wird 0 gemessen.
wenn der Fühler nichts leitet ist der Widerstand unendlich, der MessPin wird durch den eCPOwer auf high gezogen und misst 4095.

Damit ist der Messwert imgekehrt proportional zum Widerstand?! '''